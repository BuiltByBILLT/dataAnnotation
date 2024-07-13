// Retrieves initial data set.
const data0 = getData()

// Initializes an array to hold formatted data.
const data = []
// Iterates through the original data starting from index 5, incrementing by 5 each iteration.
// This implies the data is structured in a way that every 5 elements represent a new record.
for (let i = 5; i < data0.length; i += 5) {
	// Pushes an object to the 'data' array containing relevant vehicle information.
	data.push({
		Make: data0[i],
		FuelType: data0[i + 1],
		EngineCylinders: data0[i + 2],
		AverageHighwayMPG: data0[i + 3],
		AverageCityMPG: data0[i + 4],
	})
}

// Sets up margins for the SVG container.
const margin = { top: 20, right: 20, bottom: 30, left: 70 }
// Calculates the width and height of the actual visualization area (inside margins).
const width = 400 - margin.left - margin.right
const height = 400 - margin.top - margin.bottom

// Appends an SVG element to the body of the document, sets its size, and positions it.
const svg = d3
	.select("body")
	.append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.attr("style", "position: absolute; top: 100px; left: 400px")
	.append("g")
	.attr("transform", `translate(${margin.left},${margin.top})`)

// Defines linear scales for the x and y axes based on data.
var xScale = d3
	.scaleLinear()
	.domain([0, d3.max(data, d => d.EngineCylinders)])
	.range([0, width])
var yScale = d3
	.scaleLinear()
	.domain([0, d3.max(data, d => d.AverageHighwayMPG)])
	.range([height, 0])

// Adds the X and Y axes to the SVG.
svg.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(xScale))

svg.append("g").call(d3.axisLeft(yScale))

// Creates grid lines for the x and y axes for better readability of the chart.
const xAxisGrid = d3.axisBottom(xScale).tickSize(-height).tickFormat("")
const yAxisGrid = d3.axisLeft(yScale).tickSize(-width).tickFormat("")

svg.append("g").attr("class", "x axis-grid").attr("transform", `translate(0, ${height})`).call(xAxisGrid)

svg.append("g").attr("class", "y axis-grid").call(yAxisGrid)

// Function to update scatter plot based on dropdown selections.
function updateScatterplot(selection1, selection2) {
	var filteredData = data

	// Filters data based on 'FuelType' if a specific type has been selected.
	if (selection1 !== "All") {
		filteredData = data.filter(item => item.FuelType === selection1)
	}
	// Further filters data based on 'Make' if a specific make has been selected.
	if (selection2 !== "All") {
		filteredData = filteredData.filter(item => item.Make === selection2)
	}
	console.log(filteredData) // Logs the filtered data for debugging.

	// Removes all existing circles (data points) before drawing new ones.
	d3.selectAll("circle").remove()

	// Creates circles for each data point in the filtered dataset,
	// positioning and coloring them based on data attributes.
	svg
		.selectAll("circle")
		.data(filteredData)
		.enter()
		.append("circle")
		.attr("cx", d => xScale(d.EngineCylinders))
		.attr("cy", d => yScale(d.AverageHighwayMPG))
		.attr("r", 5) // Radius of circles.
		.attr("fill", d => {
			// Color coding by 'FuelType'.
			if (d.FuelType == "Electricity") return "green"
			else if (d.FuelType == "Diesel") return "yellow"
			else return "red"
		})
}

// Initial call to populate the scatterplot.
updateScatterplot("All", "All")

// Event listener for dropdown changes to update the scatterplot based on selection.
document.getElementById("dropdown").addEventListener("change", function () {
	var second_val = document.getElementById("second-dropdown").value
	const selectedOption = this.value
	updateScatterplot(selectedOption, second_val)
})

document.getElementById("second-dropdown").addEventListener("change", function () {
	var first_val = document.getElementById("dropdown").value
	const selectedOption = this.value
	updateScatterplot(first_val, selectedOption)
})
