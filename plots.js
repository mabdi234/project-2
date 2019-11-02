
    
function init() {
    data = [{
      x: data1.cities,
      y: data1.salaries}];
      
    var LINE = document.getElementById("plot");
    // Define the plot layout
    var layout = {
        title: "Average Salaries per City",
        xaxis: { title: "City" },
        yaxis: { title: "Salary" }
    };
    Plotly.plot(plot, data, layout);
  };
  
function updatePlotly(newx, newy) {
var LINE = document.getElementById("plot");

// Note the extra brackets around 'newx' and 'newy'
Plotly.restyle(LINE, "x", [newx]);
Plotly.restyle(LINE, "y", [newy]);
}

function getData(dataset) {

// Initialize empty arrays to contain our axes
var x = [];
var y = [];

// Fill the x and y arrays as a function of the selected dataset
switch (dataset) {
case "dataset1":
    x = data1.cities;
    y = data1.salaries;
    break;
case "dataset2":
    x = data2.cities;
    y = data2.salaries;
    break;
case "dataset3":
    x = data3.cities;
    y = data3.salaries;
    break;
default:
    x = data4.cities;
    y = data4.salaries;
    break;
}

updatePlotly(x, y);
};

init();