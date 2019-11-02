console.log(data)


// Create the Traces
var trace1 = {
  x: data1.cities,
  y: data1.salaries,
  mode: "markers",
  type: "scatter",
  name: "Salaries",
  marker: {
    color: "#2077b4",
    symbol: "hexagram"
  }
};



// Create the data array for the plot
var data = [trace1];

// Define the plot layout
var layout = {
  title: "Average Salaries per City",
  xaxis: { title: "City" },
  yaxis: { title: "Salary" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("plot", data, layout);
