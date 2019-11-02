// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 660;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);


// Create the Traces
var trace2 = {
    x: bar_data.company,
    y: bar_data.jobs,
    type: "bar",
    name: "Top 20 Companies",
    orientation: "h"
  };

var data = [trace2];

// Apply the group bar mode to the layout
var layout = {
    title: "Top 20 Companies",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
