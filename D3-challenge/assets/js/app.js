// SVG Canvas Parameters
const svgWidth = 800;
const svgHeight = 500;
const padding = 40;

// Building SVG Canvas
const svg1 = d3.select('#scatter')
            .append('svg')
            .attr('width', svgWidth)
            .attr('height', svgHeight)
            //.style('background-color', 'yellow');


//Reading CSV
d3.csv('assets/data/data.csv').then(function(data){

    console.log(data[0]) //test

    // Pulling and storing relevant data 
    var dataset = [];

    data.forEach(function(state){
        
        dataset.push([state.abbr, +state.poverty, +state.healthcare])

    });

    console.log(dataset) //test

    // Building Scaling Functions
    const xScale = d3.scaleLinear()
                    .domain([6, d3.max(dataset, (d) => d[1])])
                    .range([padding, svgWidth - padding]);

    const yScale = d3.scaleLinear()
                    .domain([0, d3.max(dataset, (d) => d[2])])
                    .range([svgHeight - padding, padding]);

    console.log(dataset[0][1]) //test
    console.log(xScale(19.3)) //test

    // Plotting data using circles
    svg1.selectAll('circle')
        .data(dataset)
        .enter()
        .append('circle')
        .attr('cx', (d) => xScale(d[1]))
        .attr('cy', (d) => yScale(d[2]))
        .attr('r', 10)
        .attr('class', 'stateCircle');


    // Adding text labels
    svg1.selectAll('text')
        .data(dataset)
        .enter()
        .append('text')
        .text((d) => d[0])
        .attr('x', (d) => xScale(d[1]))
        .attr('y', (d) => yScale(d[2]))
        .attr('font-size', '10px')
        .attr('text-anchor', 'middle')
        .attr('fill', 'white');

    // Adding Axes
    const xAxis = d3.axisBottom(xScale);
    svg1.append('g')
        .attr('transform', 'translate(0, ' + (svgHeight - padding) + ')')
        .call(xAxis);

    const yAxis = d3.axisLeft(yScale);
    svg1.append('g')
        .attr('transform', 'translate(' + padding + ', 0)')
        .call(yAxis);

    // Create axes labels
    svg1.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - padding + 40)
        .attr("x", 0 - (svgHeight*2 / 3))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare (%)");

    svg1.append("text")
        .attr("transform", `translate(${svgWidth / 2}, ${svgHeight - padding + 30})`)
        .attr("class", "axisText")
        .text("Poverty (%)");

});



