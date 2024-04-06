var trace1a = {
  x: x,
  y: yG,
  marker: {color: org_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var trace1b = {
  x: x,
  y: yG,
  marker: {color: grouped_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var trace1c = {
  x: x,
  y: yB,
  marker: {color: recolor_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var trace2a = {
  x: x,
  y: yB,
  marker: {color: org_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var trace2b = {
  x: x,
  y: yB,
  marker: {color: grouped_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var trace2c = {
  x: x,
  y: yB,
  marker: {color: recolor_color, size: 5},
  mode: 'markers',
  type: 'scatter',
};

var k_col_dots_G = {
  x: k_col_R,
  y: k_col_G,
  marker: {
    color: k_col_color, 
    size: 20,
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var picked_dots_G = {
  x: picked_R,
  y: picked_G,
  marker: {
    color: picked_color, 
    size: 20,
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var k_col_dots_B = {
  x: k_col_R,
  y: k_col_B,
  marker: {
    color: k_col_color, 
    size: 20,
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var picked_dots_B = {
  x: picked_R,
  y: picked_B,
  marker: {
    color: picked_color, 
    size: 20,
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var k_col_stars_G = {
  x: k_col_R,
  y: k_col_G,
  marker: {
    color: 'yellow', 
    size: 20,
    symbol: 'star',
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var picked_stars_G = {
  x: picked_R,
  y: picked_G,
  marker: {
    color: 'yellow', 
    size: 20,
    symbol: 'star',
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var k_col_stars_B = {
  x: k_col_R,
  y: k_col_B,
  marker: {
    color: 'yellow', 
    size: 20,
    symbol: 'star',
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var picked_stars_B = {
  x: picked_R,
  y: picked_B,
  marker: {
    color: 'yellow', 
    size: 20,
    symbol: 'star',
    line: {
      color: 'black',
      width: 3
    }
  },
  mode: 'markers',
  type: 'scatter',
};

var layout = {
  width: 250,
  height: 300,
  margin: {
    l: 0,
    r: 0,
    b: 0,
    t: 0,
    pad: 0
  },
  plot_bgcolor:"#EDEDED",
  paper_bgcolor:"#EDEDED",
  xaxis: {visible: false},
  yaxis: {visible: false},
};

var wide_layout = {
  width: 330,
  height: 300,
  margin: {
    l: 0,
    r: 0,
    b: 0,
    t: 0,
    pad: 0
  },
  plot_bgcolor:"#EDEDED",
  paper_bgcolor:"#EDEDED",
  xaxis: {visible: false},
  yaxis: {visible: false},
};

data = [trace1a, trace2a, trace1b, trace2b, trace1c, trace2c]

Plotly.newPlot("g1", [trace1a], layout)
Plotly.newPlot("g2", [trace1b, k_col_stars_G, picked_dots_G], wide_layout)
Plotly.newPlot("g3", [trace1c, k_col_dots_G, picked_stars_G], wide_layout)
Plotly.newPlot("g4", [trace2a], layout)
Plotly.newPlot("g5", [trace2b, k_col_stars_B, picked_dots_B], wide_layout)
Plotly.newPlot("g6", [trace2c, k_col_dots_B, picked_stars_B], wide_layout)