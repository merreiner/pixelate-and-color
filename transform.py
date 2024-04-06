import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import skimage
from skimage import io
from sklearn.cluster import KMeans
import math

myFile = sys.argv[1]
myColors = sys.argv[2]
myFactor = sys.argv[3]

def hex_to_rgb(value):
    all_colors = []
    for c in value.split(","):
        c = c.lstrip("#")
        lv = len(c)
        color = []
        for i in range(0, lv, lv // 3):
            color.append(int(c[i:i + lv // 3], 16)/255)
        all_colors.append(color)
    return all_colors

def find_closest(cluster_n, the_colors):
    distance = []
    the_color = []
    for i in the_colors:
        distance_n = math.sqrt((i[0] - cluster_n[0])**2+(i[1] - cluster_n[1])**2+(i[2] - cluster_n[2])**2)
        distance.append(distance_n)
        the_color.append(i)
    minim = min(distance)
    index = distance.index(minim)
    return the_color[index]

def pixelate_rgb(img, window):
    n, m, _ = img.shape
    n, m = n - n % window, m - m % window
    img1 = np.zeros((n, m, 3))
    for x in range(0, n, window):
        for y in range(0, m, window):
            img1[x:x+window,y:y+window] = img[x:x+window,y:y+window].max(axis=(0,1))
    return img1

def createjs(df1, df2, df3):
    text = ""
    text = text + f"var x = " + str(df1.x.to_list()) + "\n"
    text = text + f"var yG = " + str(df1.yG.to_list()) + "\n"
    text = text + f"var yB = " + str(df1.yB.to_list()) + "\n"
    text = text + f"var org_color = " + str(df1.org_color.to_list()) + "\n"
    text = text + f"var grouped_color = " + str(df1.grouped_color.to_list()) + "\n"
    text = text + f"var recolor_color = " + str(df1.recolor_color.to_list()) + "\n"
    text = text + f"var k_col_R = " + str(df2.R.to_list()) + "\n"
    text = text + f"var k_col_G = " + str(df2.G.to_list()) + "\n"
    text = text + f"var k_col_B = " + str(df2.B.to_list()) + "\n"
    text = text + f"var k_col_color = " + str(df2.formatted_colors.to_list()) + "\n"
    text = text + f"var picked_R = " + str(df3.R.to_list()) + "\n"
    text = text + f"var picked_G = " + str(df3.G.to_list()) + "\n"
    text = text + f"var picked_B = " + str(df3.B.to_list()) + "\n"
    text = text + f"var picked_color = " + str(df3.formatted_colors.to_list()) + "\n"
    return text

def main():
    
    chosen_colors = hex_to_rgb(myColors)
    
    img=io.imread('./public/images/'+myFile)
    image_shape = img.shape

    num_of_colors=len(chosen_colors)

    pixel_factor = int(myFactor)

    # transform the original data
    img_data = (img/255.0).reshape(-1,3)
    og_color = pd.DataFrame(img_data, columns=['R', 'G', 'B'])
    og_color['colors'] = og_color.apply(lambda r: tuple(r), axis=1).apply(np.array)
    og_color['formatted_colors'] = og_color.apply(lambda r: f"rgba({int(r[0]*255)},{int(r[1]*255)},{int(r[2]*255)},0.7)" , axis=1)

    kmeans = KMeans(n_clusters=num_of_colors).fit(img_data)
    k_colors=kmeans.cluster_centers_[kmeans.predict(img_data)]

    # create grouped colors dataframe with the new k_colors given
    grouped_colors = pd.DataFrame(k_colors, columns=['R', 'G', 'B'])
    grouped_colors['colors'] = grouped_colors.apply(lambda r: tuple(r), axis=1).apply(np.array)
    grouped_colors['formatted_colors'] = grouped_colors.apply(lambda r: f"rgba({int(r[0]*255)},{int(r[1]*255)},{int(r[2]*255)},0.7)" , axis=1)

    # create lego colors dataframe with the lego palatte
    picked_colors = pd.DataFrame(chosen_colors, columns=['R', 'G', 'B'])
    picked_colors['colors'] = picked_colors.apply(lambda r: tuple(r), axis=1).apply(np.array).apply(str)
    picked_colors['formatted_colors'] = picked_colors.apply(lambda r: f"rgba({int(r[0]*255)},{int(r[1]*255)},{int(r[2]*255)},0.7)" , axis=1)

    # create dataframe with k color points
    the_k_colors = grouped_colors.drop_duplicates(subset=["formatted_colors"], keep='first')
    
    # create an array of the centroids
    identified_palette = np.array(kmeans.cluster_centers_)

    # match the closest lego color to each centroid
    the_colors = []
    for i in identified_palette:
        k = find_closest(i, chosen_colors)
        the_colors.append(k)

    the_colors = np.array(the_colors)

    # find out which cluster each pixel belongs to
    labels = kmeans.predict(img_data)

    # make a copy of image data to recolor
    recolored_img = np.copy(img_data)

    # recolor the image data
    for index in range(len(recolored_img)):
        recolored_img[index] = the_colors[labels[index]]

    recolored_colors = pd.DataFrame(recolored_img, columns=['R', 'G', 'B'])
    recolored_colors['colors'] = recolored_colors.apply(lambda r: tuple(r), axis=1).apply(np.array)
    recolored_colors['formatted_colors'] = recolored_colors.apply(lambda r: f"rgba({int(r[0]*255)},{int(r[1]*255)},{int(r[2]*255)},0.7)" , axis=1)

    # reshape to image shape
    recolored_img = recolored_img.reshape(image_shape)

    pixel_img = pixelate_rgb(recolored_img, pixel_factor)

    io.imsave('./public/editedimages/'+myFile, pixel_img)
    
    total_data = pd.DataFrame({"x": og_color.R, "yG": og_color.G, "yB": og_color.B, "org_color": og_color.formatted_colors, "grouped_color": grouped_colors.formatted_colors, "recolor_color": recolored_colors.formatted_colors}).sample(frac=0.05)

    with open('./public/data.js', 'w') as f:
        f.write(createjs(total_data, the_k_colors, picked_colors))

    print()
    
main()