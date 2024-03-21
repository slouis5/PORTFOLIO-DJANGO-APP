window.onload = function() {
    var elements = document.querySelectorAll('.skill_cat_container');
    var index = 0;
  
    function displayNextElement() {
      // Hide all elements
      elements.forEach(function(element) {
        element.style.display = 'none';
      });
  
      // Display the next element
      elements[index].style.display = 'block';
      //elements[index].style.animation = '3s linear 1s infinite running slidein';
      index = (index + 1) % elements.length; // Wrap around to the beginning if end is reached
  
      // Call the function again after 2 seconds
      setTimeout(displayNextElement, 3000);
    }
  
    // Start displaying elements with delay
    displayNextElement();

    const imageContainer = document.querySelector('#company_band');
    const images = document.querySelectorAll('#company_band img');
    const cloneImages = Array.from(images).map(img => img.cloneNode(true));
  
    cloneImages.forEach(cloneImg => imageContainer.appendChild(cloneImg));
  };
  
  