// Select the buttons
var allrestaurant = d3.select(".allrestaurants");
var availabletime = d3.select(".availabletimes");

// Select the printer elements
var allbox = d3.select(".allresbox");
var availbox = d3.select(".availresbox")

// Use D3 `.on` to attach a click handler for all restaurants
  allrestaurant.on("click", function() {
    // Select the info
    var allinfo = 
  
    // Set the all restaurant box text to the new info
    allresbox.text(allinfo);
  });
  
  // Use d3 `.on` to attach a click handler for the available restaurants
  availabletime.on("click", function() {
    // Select the info
    var availinfo = 
  
  
    // Set the available restauant text to the new info
    availbox.text(availinfo);
  });