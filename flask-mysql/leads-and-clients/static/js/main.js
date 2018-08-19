window.onload = function() {
  var options = {
    title: {
      text: "Years in Office"
    },
    animationEnabled: true,
    data: [{
      type: "pie",
      startAngle: 40,
      toolTipContent: "{label} {y}",
      showInLegend: "true",
      legendText: "{label}",
      indexLabelFontSize: 16,
      indexLabel: "{label} {y}",
      dataPoints: [
        {% for friend in friends %} {
          y: {{friend['years_in_office']}},
          label: "{{friend['last_name']}}"
        },
        {% endfor %}
      ]
    }]
  };
  $("#chartContainer").CanvasJSChart(options);
}
