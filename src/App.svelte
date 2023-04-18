 
<script>

  import './styles.css';
  import logo from './assets/top-logo-full.svg';

  import colours from './lib/colours.json';

  import { onMount } from 'svelte'
  import mapboxgl from "mapbox-gl";

  mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2xhYjg0ZTl3MDIydDN3b3MzZmV4dXIydSJ9.lR7rnaKdBdTNGcc2kGDPbQ';
  
  let map;
  
  let pageWidth;

  let added_languages=[];

  const maxBounds = [
		[-81.0, 42.4], // SW coords
		[-78.0, 45.0] // NE coords
	];

  let ctuid = 0
  let languagelist = ['Bosnian', 'Croatian', 'Dari', 'Iranian Persian', 'Odia', 'Serbian', 'Afrikaans', 'Assyrian Neo-Aramaic', 'Belarusian', 'Bengali', 'Bulgarian', 'Chaldean Neo-Aramaic', 'Czech', 'Danish', 'Dutch', 'German', 'Gujarati', 'Hindi', 'Kacchi', 'Konkani', 'Kurdish', 'Latvian', 'Lithuanian', 'Macedonian', 'Marathi', 'Nepali', 'Norwegian', 'Pashto', 'Polish', 'Punjabi (Panjabi)', 'Russian', 'Serbo-Croatian', 'Sindhi', 'Sinhala (Sinhalese)', 'Slovak', 'Slovene (Slovenian)', 'Swedish', 'Ukrainian', 'Urdu', 'Yiddish', 'Amharic', 'Arabic', 'Hakka', 'Harari', 'Hausa', 'Hebrew', 'Irish', 'Italian', 'Maltese', 'Mandarin', 'Min Dong', 'Min Nan (Chaochow, Teochow, Fukien, Taiwanese)', 'Oromo', 'Portuguese', 'Romanian', 'Somali', 'Spanish', 'Tibetan', 'Tigrigna', 'Wu (Shanghainese)', 'Yue (Cantonese)', 'Akan (Twi)', 'Albanian', 'American Sign Language', 'Armenian', 'Azerbaijani', 'Cebuano', 'Coptic', 'Edo', 'Estonian', 'Finnish', 'Ga', 'Ganda', 'Greek', 'Haitian Creole', 'Hiligaynon', 'Hungarian', 'Igbo', 'Ilocano', 'Indonesian', 'Jamaican English Creole', 'Kannada', 'Khmer (Cambodian)', 'Lao', 'Lingala', 'Malay', 'Malayalam', 'Morisyen', 'Pampangan (Kapampangan, Pampango)', 'Rundi (Kirundi)', 'Shona', 'Swahili', 'Tagalog (Pilipino, Filipino)', 'Tamil', 'Telugu', 'Thai', 'Tulu', 'Turkish', 'Vietnamese', 'Yoruba', 'Georgian', 'Japanese', 'Korean', 'English', 'French', 'Other'].reverse()

  onMount(() => {
    map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/schoolofcities/clddge3j0006q01o7fi0p3xyq',
      center: [-79.32, 43.775], 
			zoom: 10,
			maxZoom: 13.5,
			minZoom: 2,
			bearing: -17.7,
			maxBounds: maxBounds,
      projection: 'globe',
      bearing: -17.1
    });
 
    map.on('style.load', () => {
      map.setFog({}); 
    });

    map.addControl(new mapboxgl.NavigationControl(), 'top-left');
  
    map.on('load', () => {
      
      map.addSource("languages", {
        "type": "geojson",
        "data": "data/rand_points_spoken_languages_GTA_no_water_final2.geojson"
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
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-stroke-color": [
          'match',
          ['get', 'Language'],
          feature,
          colours[feature],
          '#ccc'
        ],
        "circle-opacity": 0.25,
        "circle-color": [
          'match',
          ['get', 'Language'],
          feature,
          colours[feature],
          '#ccc'
        ]
        }
      });
    });

  
      
      // When a click event occurs on a feature in the places layer, open a popup at the
      // location of the feature, with description HTML from its properties.
      for (const id of languagelist) {
      map.on('click', id, (e) => {
      // Copy coordinates array.
      const coordinates = e.features[0].geometry.coordinates.slice();
      const language = e.features[0].properties.Language.trim();
      const speaker = e.features[0].properties.Speaker_No.toString();
      
      // Ensure that if the map is zoomed out such that multiple
      // copies of the feature are visible, the popup appears
      // over the copy being pointed to.
      while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
      coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
      }
      
      let popup=new mapboxgl.Popup()
      .setLngLat(coordinates)
      .setHTML(language + ',\n' +speaker)
      .addTo(map);

      var features = map.queryRenderedFeatures(e.point, {layers:['gtha-da-2021']});
        if (ctuid != features[0].properties.DAUID) {
          var style = [
            "match",
            ["get", "DAUID"],
            [features[0].properties.DAUID],
            "#f1c500",
            'transparent'
          ]
          map.setPaintProperty('gtha-da-2021', 'fill-color', style)
          ctuid = features[0].properties.DAUID
        } else {
          map.setPaintProperty('gtha-da-2021', 'fill-color', 'transparent')
          ctuid = 0
        }

      popup.on('close', () => {
        map.setPaintProperty('gtha-da-2021', 'fill-color', 'transparent')})
        ctuid = 0
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

      const layers = [
      '500',
      '1000'
        ];
      const sizes = [
        '28px',
        '63px'
        ];
  
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
          document.getElementById("color1").style.fill = colours['Punjabi (Panjabi)']
          document.getElementById("color1").style.stroke = colours['Punjabi (Panjabi)']
          var img = document.getElementById("circle1");
          var newimg21 = img.cloneNode(true);
          link.appendChild(newimg21);
          link.insertAdjacentText('beforeend', ` ${id}`);
          }

          if (id == 'Italian'){
          document.getElementById("color1").style.fill = colours['Italian']
          document.getElementById("color1").style.stroke = colours['Italian']
          var img = document.getElementById("circle1");
          var newimg25 = img.cloneNode(true);
          link.appendChild(newimg25);
          link.insertAdjacentText('beforeend', ` ${id}`);
          }

          if (id == 'Mandarin'){
          document.getElementById("color1").style.fill = colours['Mandarin']
          document.getElementById("color1").style.stroke = colours['Mandarin']
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
        map.setFilter(feature, ['==', 'Language', feature]);
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
    document.getElementById("color1").style.fill = colours[feature];
    document.getElementById("color1").style.stroke = colours[feature];
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
    <circle id="color1" cx="8" cy="8" r="5" stroke="black" stroke-width="1.5" fill="#ffffff" />
  </svg>

  <div id="panel">

    <div id="title">
      <h1>Knowledge of Languages in the Greater Toronto & Hamilton Area</h1>
    </div>

    <nav id="menu">
    </nav>

    <input id="feature-filter" type="text" placeholder="Search For Languages (Click Above To Remove)">

    <div id="feature-listing" class="listing"></div>
    
    <div id="info">
      <div id='legend'>
        <svg height="74" width="200">
          <circle cx="50" cy="40" r="32" stroke="black" stroke-width="1" fill="white" />
          <circle cx="50" cy="61" r="10" stroke="black" stroke-width="1" fill="white" />
          <line x1="65" y1="9" x2="100" y2="9" stroke="black" stroke-dasharray="4 1 4 1" />
          <line x1="58" y1="51" x2="100" y2="51" stroke="black" stroke-dasharray="4 1 4 1"/>
          <text x="102" y="17" class="svg-text">5,000 speakers</text>
          <text x="102" y="59" class="svg-text">500 speakers</text>
        </svg>
      </div>
    </div>

    <div id="info">
      <p>
        This map uses the <em>Knowledge of languages</em> 25% sample data from Statistics Canada's 2021 census.
      </p>
    </div>

    <div id="logo">
      <a href="https://www.schoolofcities.utoronto.ca/"><img src={logo} alt="School of Cities"></a>
    </div>

  </div>

  <div id="map">
  </div>

</main>



<style>

</style>
