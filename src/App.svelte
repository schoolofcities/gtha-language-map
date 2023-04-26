 
<script>

  import './styles.css';
  import logo from './assets/top-logo-full.svg';

  import languageTotalColours from './lib/language-colours-speakers.json';

  import { onMount } from 'svelte'
  import mapboxgl from "mapbox-gl";

  mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2xhYjg0ZTl3MDIydDN3b3MzZmV4dXIydSJ9.lR7rnaKdBdTNGcc2kGDPbQ';
  
  let map;

  let dauid = 0;
  

  let added_languages=[];


  const maxBounds = [
		[-81.0, 42.4], // SW coords
		[-78.0, 45.0] // NE coords
	];

  let ctuid = 0
  let languagelist = languageTotalColours
    .filter(item => item.Speakers > 0)
    .map(item => item.Language);
  
  onMount(() => {
    map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/schoolofcities/clddge3j0006q01o7fi0p3xyq',
      center: [-79.40, 43.78], 
			zoom: 10,
			maxZoom: 13.5,
			minZoom: 2,
			bearing: -17.7,
			maxBounds: maxBounds,
      projection: 'globe'
    });
 
    map.on('style.load', () => {
      map.setFog({}); 
    });

    map.addControl(new mapboxgl.NavigationControl({showZoom: false}), 'top-right');

    map.addControl(new mapboxgl.NavigationControl({showCompass: false}), 'top-left');

    map.addControl(new mapboxgl.ScaleControl(), 'bottom-right');
  
    map.on('load', () => {
      
      map.addSource("languages", {
        "type": "geojson",
        "data": "data/gtha-da-2021-language-dots.geojson"
      });

      languagelist.forEach((feature) => {

        map.addLayer({
        "id": feature,
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 's'], 5]],
        "circle-stroke-width": 1,
        "circle-stroke-color": [
          'match',
          ['get', 'l'],
          feature,
          languageTotalColours.find(item => item.Language === feature).Colour,
          '#ccc'
        ],
        "circle-opacity": 0.25,
        "circle-color": [
          'match',
          ['get', 'l'],
          feature,
          languageTotalColours.find(item => item.Language === feature).Colour,
          '#ccc'
        ]
        }
      });
    });

    
    
      
    for (const id of languagelist) {
      map.on('click', id, (e) => {

        // base grab info
        const coordinates = e.features[0].geometry.coordinates.slice();
        const language = e.features[0].properties.l.trim();
        const speaker = e.features[0].properties.s.toString();
        dauid = e.features[0].properties.d;

        // // Ensure that if the map is zoomed out such that multiple
        // // copies of the feature are visible, the popup appears
        // // over the copy being pointed to.
        // while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
        //   coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        // }

        let popup = new mapboxgl.Popup()
          .setLngLat(coordinates)
          .setHTML("<b>" + speaker + "</b> " + language + " Speakers")
          .addTo(map);

        map.setFilter('gtha-da-2021',[
          "all",
          [
            "match",
            ["get", "DAUID"],
            [dauid.toString()],
            true,
            false
          ]
        ]);

        console.log(dauid);

        // var features = map.queryRenderedFeatures(e.point, { layers: ['gtha-da-2021'] });
        // var style = [
        //     "match",
        //     ["get", "DAUID"],
        //     dauid.toString(),
        //     "#000000",
        //     '#ffffff'
        //   ]
        // map.setPaintProperty('gtha-da-2021', 'fill-color', style) 
        
        popup.on('close', () => {
          dauid = 0;
          map.setFilter('gtha-da-2021',[
          "all",
          [
            "match",
            ["get", "DAUID"],
            [dauid.toString()],
            true,
            false
          ]
        ]);
        })
        
      });

      // Change the cursor to a pointer when the mouse is over the places layer.
      map.on('mouseenter', id, () => {
        map.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      map.on('mouseleave', id, () => {
        map.getCanvas().style.cursor = '';
      });
    }

      
  






        filterEl.addEventListener('keyup', (e) => {
        const value = normalize(e.target.value);
        
        // Filter visible features that match the input value.
        const filtered = [];
        for (const feature of languagelist) {
        //const name = normalize(feature.properties.Language);
        if (normalize(feature).includes(value) && value!='' && added_languages.includes(feature)==false) {
        filtered.push(feature);
        }
        }
        //SORT HERE
        const sortBySubstring = (words, match) => {
          return words.sort((a, b) => {
            return a.indexOf(match) - b.indexOf(match);
          });
        }

        const result = sortBySubstring(filtered, e.target.value);
        // Populate the sidebar with filtered results
        renderListings(result.slice(0,5));
        //renderListings(filtered);
        
        });
        
        // Call this function on initialization
        // passing an empty array to render an empty state
        renderListings([]);
        
        for (const id of languagelist){
          if (id ==='Italian' || id ==='Mandarin' || id==='Punjabi (Panjabi)') {
          added_languages.push(id)
          const link = document.createElement('a');
          link.id = id;
          link.href = '#';
          //link.textContent = 'X '+id; //'X '+id;
          link.className = 'active';
          const clickedLayer = id;
          map.setLayoutProperty(clickedLayer, 'visibility', 'visible');

          if (id == 'Punjabi (Panjabi)'){
          document.getElementById("color1").style.fill = languageTotalColours.find(item => item.Language === 'Punjabi (Panjabi)').Colour          
          document.getElementById("color1").style.stroke = languageTotalColours.find(item => item.Language === 'Punjabi (Panjabi)').Colour
          var img = document.getElementById("circle1");
          var newimg21 = img.cloneNode(true);
          link.appendChild(newimg21);
          link.insertAdjacentText('beforeend', ` ${id}`);
          }

          if (id == 'Italian'){
          document.getElementById("color1").style.fill = languageTotalColours.find(item => item.Language === 'Italian').Colour
          document.getElementById("color1").style.stroke = languageTotalColours.find(item => item.Language === 'Italian').Colour
          var img = document.getElementById("circle1");
          var newimg25 = img.cloneNode(true);
          link.appendChild(newimg25);
          link.insertAdjacentText('beforeend', ` ${id}`);
          }

          if (id == 'Mandarin'){
          document.getElementById("color1").style.fill = languageTotalColours.find(item => item.Language === 'Mandarin').Colour
          document.getElementById("color1").style.stroke = languageTotalColours.find(item => item.Language === 'Mandarin').Colour
          var img = document.getElementById("circle1");
          var newimg17 = img.cloneNode(true);
          link.appendChild(newimg17);
          link.insertAdjacentText('beforeend', ` ${id}`);
          }
          const layers = document.getElementById('menu');
          layers.appendChild(link);
          }
        } 

      languagelist.forEach((feature) => {
        map.setFilter(feature, ['==', 'l', feature]);
      });
     
    });
    
    map.on('idle', () => {
      languagelist.forEach((feature) => {
      if (!map.getLayer(feature)){
        return;
      }
    });

  });






  const filterEl = document.getElementById('feature-filter');
  const listingEl = document.getElementById('feature-listing');
    
  function renderListings(features) {
    const empty = document.createElement('p');
    // Clear any existing listings
    listingEl.innerHTML = '';
    for (const feature of features) {
    const itemLink = document.createElement('a');
    const label = `${feature}`;
    itemLink.target = '_blank';
    itemLink.textContent = label;

    listingEl.appendChild(itemLink);
    itemLink.addEventListener('click', () => {

    trial(feature)
    });
    }
    
    // Show the filter input
    filterEl.parentNode.style.display = 'block';
    }
    
    function normalize(string) {
    return string.trim().toLowerCase();
    }

    function trial(feature) {
      added_languages.push(feature)
      renderListings([]);
      document.getElementById('feature-filter').value=''
      const link = document.createElement('a');
      link.id = feature;
      link.href = '#';
      //link.textContent = feature; //'X '+ feature
      link.className = '';
    
   
      const clickedLayer = feature;
      map.setLayoutProperty(clickedLayer, 'visibility', 'visible');
      link.className = 'active';
      //e.preventDefault();
      //e.stopPropagation();
    
    
    const layers = document.getElementById('menu');
    layers.appendChild(link);
    document.getElementById("color1").style.fill = languageTotalColours.find(item => item.Language === feature).Colour;
    document.getElementById("color1").style.stroke = languageTotalColours.find(item => item.Language === feature).Colour;
    var img = document.getElementById("circle1");
    var newimg = img.cloneNode(true);
    link.appendChild(newimg);
    link.insertAdjacentText('beforeend', ` ${feature}`);
  }

    
  

  map.on('idle', () => {
      languagelist.forEach((feature) => {
      if (!map.getLayer(feature)){
        return;
      }
     });
        
      for (const id of languagelist) {
        
        if (document.getElementById(id)) {
          const getlink = document.getElementById(id)

          getlink.onclick = function (e) {

            added_languages.splice(added_languages.indexOf(id), 1)
            const clickedLayer = this.textContent.substring(1); //2
            e.preventDefault();
            e.stopPropagation();
          
            map.setLayoutProperty(clickedLayer, 'visibility', 'none');
            const layers = document.getElementById('menu');
            layers.removeChild(getlink);
           
          };
          
          
          }
        } 
      });
    
  });


</script>




<main>

  <svg id="circle1" height="14" width="14">
    <circle id="color1" cx="8" cy="8" r="5" stroke="black" stroke-width="1.5"  />
  </svg>

  <div id="panel">

    <div id="title">
      <h1>Knowledge of Languages in the Greater Toronto & Hamilton Area.</h1>
    </div>


    <nav id="menu">
    </nav>

    <input id="feature-filter" type="text" placeholder="Search For Languages (Click Above To Remove)">

    <div id="feature-listing" class="listing"></div>

    
    <div id="info">
      
      <p>The size of each dot on the map represents the number of speakers within a census Dissemination Area (DA). Click on a dot to show the count and DA boundary.
      </p>

      <div id='legend'>
        <svg height="74" width="157">
          <circle cx="33" cy="40" r="32" stroke="gray" stroke-width="1" fill="white" fill-opacity="0.1" />
          <circle cx="33" cy="61" r="10" stroke="gray" stroke-width="1" fill="white" fill-opacity="0.1" />
          <line x1="50" y1="9" x2="80" y2="9" stroke="black" stroke-dasharray="4 1 4 1" />
          <line x1="44" y1="51" x2="80" y2="51" stroke="black" stroke-dasharray="4 1 4 1"/>
          <text x="82" y="15" class="svg-text">5,000 speakers</text>
          <text x="82" y="58" class="svg-text">500 speakers</text>
        </svg>
      </div>
    </div>

    <div id="after">
      <p>
        Data are from the 2021 Canadian Census, and pertain to the number of people who <a href="https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/Definition-eng.cfm?ID=pop054">"can conduct a conversation"</a>, in the specified language. 
      Those noted with <b>n.i.e.</b> denote "not included elsewhere", and <b>n.o.s.</b> denote "not otherwise specified".
      </p><p>
        This map was built by <a href="https://www.linkedin.com/in/anamariazamrii/">Ana-Maria Zamrii</a> and <a href = "http://jamaps.github.io/">Jeff Allen</a>. Code and data are on <a href="https://github.com/schoolofcities/gtha-language-map">GitHub</a>.
      </p>
    </div>

    <div id="logo">
      <a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
    </div>

  </div>

  <div id="map">
  </div>

</main>
