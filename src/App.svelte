

<script>

  import { onMount } from 'svelte'
  import mapboxgl from "mapbox-gl";

  mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w2Z2xhOXprMTYzczNlcHNjMnNvdGlmNCJ9.lOgVHrajc1L-LlU0as2i2A';
  
  let map;
  
  let pageWidth;

  const maxBounds = [
		[-80.161139, 43.286294], // SW coords
		[-78.436960, 44.516575] // NE coords
	];

  onMount(() => {
    map = new mapboxgl.Map({
      container: 'map', // container ID
      style: 'mapbox://styles/mapbox/light-v10', // style URL
      //zoom: 2, // starting zoom
      //center: [108, 4], // // starting center in [lng, lat]
      center: [-79.22, 43.765], 
			zoom: 12,
			maxZoom: 13.5,
			minZoom: 2,
			bearing: -17.7,
			maxBounds: maxBounds,
      projection: 'globe', // display map as a 3D globe
      bearing: -17.1
    });
 
    map.on('style.load', () => {
      map.setFog({}); // enable atmosphere and stars
    });
  
    map.on('load', () => {

      map.addSource("gta", {
      "type": "geojson",
      "data": "data/gta.geojson"
      });
      
      map.addLayer(
      {
      "id": "gta",
      "type": "fill",
      "source": "gta",
      "paint": {
      "fill-outline-color": "#000000",
      "fill-color": "#CBC3E3",
      "fill-opacity": 0.5
      }
      }
      );
      
      map.addSource("languages", {
      "type": "geojson",
      "data": "data/no_water_commercial_industrial.geojson"
      });

      //English 

       map.addLayer({
        "id": "English",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "visible"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '      English',
          '#FFCCCB',

        
          /* other */ '#ccc'
        ]
        }
      });

      //Mandarin
      map.addLayer({
        "id": "Mandarin",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "visible"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Mandarin',
          '#ff0000',
          /* other */ '#ccc'
        ]
        }
      });



      //Cantonese 
  
      map.addLayer({
        "id": "Cantonese",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "visible"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Yue (Cantonese)',
          '#2b13ff',
          /* other */ '#ccc'
        ]
        }
      });

      //Punjabi

      map.addLayer({
        "id": "Punjabi",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "visible"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Punjabi (Panjabi)',
          '#7f6646',
          /* other */ '#ccc'
        ]
        }
      });



      //Spanish

      map.addLayer({
        "id": "Spanish",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Spanish',
          '#ff7f00',
          /* other */ '#ccc'
        ]
        }
      });



      //Urdu

      map.addLayer({
        "id": "Urdu",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Urdu',
          '#1f78b4',
          /* other */ '#ccc'
        ]
        }
      });



      //Italian

      map.addLayer({
        "id": "Italian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Italian',
          '#00fff7',
          /* other */ '#ccc'
        ]
        }
      });


      //Tagalog

      map.addLayer({
        "id": "Tagalog",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Tagalog (Pilipino, Filipino)',
          '#7b71f7',
          /* other */ '#ccc'
        ]
        }
      });


      //Tamil

      map.addLayer({
        "id": "Tamil",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Tamil',
          '#ffee00',
          /* other */ '#ccc'
        ]
        }
      });


       //Arabic

      map.addLayer({
        "id": "Arabic",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Arabic',
          '#fb9a99',
          /* other */ '#ccc'
        ]
        }
      });


      //Portuguese

      map.addLayer({
        "id": "Portuguese",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Portuguese',
          '#33a02c',
          /* other */ '#ccc'
        ]
        }
      });



       //Iranian Persian

      map.addLayer({
        "id": "Iranian-Persian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '                Iranian Persian',
          '#fdbf6f',
          /* other */ '#ccc'
        ]
        }
      });



       //Russian

      map.addLayer({
        "id": "Russian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Russian',
          '#034493',
          /* other */ '#ccc'
        ]
        }
      });


       //French

      map.addLayer({
        "id": "French",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '      French',
          '#ad7400',
          /* other */ '#ccc'
        ]
        }
      });



      //Gujarati

      map.addLayer({
        "id": "Gujarati",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Gujarati',
          '#ceb25d',
          /* other */ '#ccc'
        ]
        }
      });



      //Polish

      map.addLayer({
        "id": "Polish",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Polish',
          '#cbb5ff',
          /* other */ '#ccc'
        ]
        }
      });



      //Hindi

      map.addLayer({
        "id": "Hindi",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Hindi',
          '#6a6a6a',
          /* other */ '#ccc'
        ]
        }
      });


      //Korean

      map.addLayer({
        "id": "Korean",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '        Korean',
          '#d400ff',
          /* other */ '#ccc'
        ]
        }
      });



      //Vietnamese

      map.addLayer({
        "id": "Vietnamese",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Vietnamese',
          '#8b34be',
          /* other */ '#ccc'
        ]
        }
      });


      //Bengali

      map.addLayer({
        "id": "Bengali",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Bengali',
          '#edf907',
          /* other */ '#ccc'
        ]
        }
      });



      //Greek

      map.addLayer({
        "id": "Greek",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Greek',
          '#5abde8',
          /* other */ '#ccc'
        ]
        }
      });


      //German

      map.addLayer({
        "id": "German",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              German',
          '#000000',
          /* other */ '#ccc'
        ]
        }
      });


      //Ukrainian

      map.addLayer({
        "id": "Ukrainian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '              Ukrainian',
          '#ffc800',
          /* other */ '#ccc'
        ]
        }
      });



      //Serbian

      map.addLayer({
        "id": "Serbian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '                Serbian',
          '#720808',
          /* other */ '#ccc'
        ]
        }
      });



      //Dari

      map.addLayer({
        "id": "Dari",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '                Dari',
          '#cc67bd',
          /* other */ '#ccc'
        ]
        }
      });



      //Romanian

      map.addLayer({
        "id": "Romanian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '            Romanian',
          '#ffffff',
          /* other */ '#ccc'
        ]
        }
      });



      //Malayalam

      map.addLayer({
        "id": "Malayalam",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Malayalam',
          '#8cff00',
          /* other */ '#ccc'
        ]
        }
      });


      //Croatian

      map.addLayer({
        "id": "Croatian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '                Croatian',
          '#af8080',
          /* other */ '#ccc'
        ]
        }
      });


      //Turkish

      map.addLayer({
        "id": "Turkish",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Turkish',
          '#7393B3',
          /* other */ '#ccc'
        ]
        }
      });



      //Hungarian

      map.addLayer({
        "id": "Hungarian",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Hungarian',
          '#176426',
          /* other */ '#ccc'
        ]
        }
      });



      //Telugu

      map.addLayer({
        "id": "Telugu",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          '          Telugu',
          '#cdc9ff',
          /* other */ '#ccc'
        ]
        }
      });



      //Other

      map.addLayer({
        "id": "Other",
        "type": "circle",
        "source": "languages",
        "layout": {
            "visibility": "none"
        },
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 5]],
        "circle-stroke-width": 1,
        "circle-color": [
          'match',
          ['get', 'Language'],
          'Other',
          '#b2df8a',
          /* other */ '#ccc'
        ]
        }
      });

       const languagelist = ['English', 'Mandarin', 'Cantonese', 'Punjabi', 'Spanish', 'Urdu', 'Italian', 'Tagalog', 'Tamil', 'Arabic', 'Portuguese','Iranian-Persian', 'Russian', 'French', 'Gujarati', 'Polish', 'Hindi', 'Korean', 'Vietnamese', 'Bengali', 'Greek', 'German', 'Ukrainian', 'Serbian', 'Dari', 'Romanian', 'Malayalam', 'Croatian', 'Turkish', 'Hungarian', 'Telugu', 'Other'];
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
      
      new mapboxgl.Popup()
      .setLngLat(coordinates)
      .setHTML(language + ',\n' +speaker)
      .addTo(map);
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

      const legend = document.getElementById('legend');

      layers.forEach((layer, i) => {
        const color = '#FFEDA0'; //colors[i]
        const item = document.createElement('div');
        const key = document.createElement('span');
        key.className = 'legend-key';
        key.style.backgroundColor = color;
        key.style.borderRadius = "50%";
        key.style.width = sizes[i];
        key.style.height = sizes[i];
        key.style.verticalAlign = 'middle';

        const value = document.createElement('span');
        value.innerHTML = `${layer}`;
        item.appendChild(key);
        item.appendChild(value);
        legend.appendChild(item);
      });
      map.setFilter('Mandarin', ['==', 'Language', '            Mandarin']);
      map.setFilter('Cantonese', ['==', 'Language', '            Yue (Cantonese)']);
      map.setFilter('Punjabi', ['==', 'Language', '              Punjabi (Panjabi)']);
      map.setFilter('Spanish', ['==', 'Language', '            Spanish']);
      map.setFilter('Urdu', ['==', 'Language', '              Urdu']);
      map.setFilter('Italian', ['==', 'Language', '            Italian']);
      map.setFilter('Tagalog', ['==', 'Language', '          Tagalog (Pilipino, Filipino)']);
      map.setFilter('Tamil', ['==', 'Language', '          Tamil']);
      map.setFilter('Arabic', ['==', 'Language', '            Arabic']);
      map.setFilter('Portuguese', ['==', 'Language', '            Portuguese']);
      map.setFilter('Iranian-Persian', ['==', 'Language', '                Iranian Persian']);
      map.setFilter('Russian', ['==', 'Language', '              Russian']);
      map.setFilter('French', ['==', 'Language', '      French']);
      map.setFilter('Gujarati', ['==', 'Language', '              Gujarati']);
      map.setFilter('Polish', ['==', 'Language', '              Polish']);
      map.setFilter('Hindi', ['==', 'Language', '              Hindi']);
      map.setFilter('Korean', ['==', 'Language', '        Korean']);
      map.setFilter('Vietnamese', ['==', 'Language', '          Vietnamese']);
      map.setFilter('Bengali', ['==', 'Language', '              Bengali']);
      map.setFilter('Greek', ['==', 'Language', '          Greek']);
      map.setFilter('German', ['==', 'Language', '              German']);
      map.setFilter('Ukrainian', ['==', 'Language', '              Ukrainian']);
      map.setFilter('Serbian', ['==', 'Language', '                Serbian']);
      map.setFilter('Dari', ['==', 'Language', '                Dari']);
      map.setFilter('Romanian', ['==', 'Language', '            Romanian']);
      map.setFilter('Malayalam', ['==', 'Language', '          Malayalam']);
      map.setFilter('Croatian', ['==', 'Language', '                Croatian']);
      map.setFilter('Turkish', ['==', 'Language', '          Turkish']);
      map.setFilter('Hungarian', ['==', 'Language', '          Hungarian']);
      map.setFilter('Telugu', ['==', 'Language', '          Telugu']);
      map.setFilter('Other', ['==', 'Language', 'Other']);
      map.setFilter('English', ['==', 'Language', '      English']);
    });
    
    

    map.on('idle', () => {
      if (!map.getLayer('English') || !map.getLayer('Mandarin') || !map.getLayer('Cantonese') || !map.getLayer('Punjabi') || !map.getLayer('Spanish') || !map.getLayer('Urdu') || !map.getLayer('Italian') || !map.getLayer('Tagalog') || !map.getLayer('Tamil') || !map.getLayer('Arabic') || !map.getLayer('Portuguese') || !map.getLayer('Iranian-Persian') || !map.getLayer('Russian') || !map.getLayer('French') || !map.getLayer('Gujarati') || !map.getLayer('Polish') || !map.getLayer('Hindi') || !map.getLayer('Korean') || !map.getLayer('Vietnamese') || !map.getLayer('Bengali') || !map.getLayer('Greek') || !map.getLayer('German') || !map.getLayer('Ukrainian') || !map.getLayer('Serbian') || !map.getLayer('Dari') || !map.getLayer('Romanian') || !map.getLayer('Malayalam') || !map.getLayer('Croatian') || !map.getLayer('Turkish') || !map.getLayer('Hungarian') || !map.getLayer('Telugu') || !map.getLayer('Other') )  {
        return;
      }
    
   
      const toggleableLayerIds = ['English', 'Mandarin', 'Cantonese', 'Punjabi', 'Spanish', 'Urdu', 'Italian', 'Tagalog', 'Tamil', 'Arabic', 'Portuguese','Iranian-Persian', 'Russian', 'French', 'Gujarati', 'Polish', 'Hindi', 'Korean', 'Vietnamese', 'Bengali', 'Greek', 'German', 'Ukrainian', 'Serbian', 'Dari', 'Romanian', 'Malayalam', 'Croatian', 'Turkish', 'Hungarian', 'Telugu', 'Other'];
    
      for (const id of toggleableLayerIds) {
        if (document.getElementById(id)) {
          continue;
        }
    

      const link = document.createElement('a');
      link.id = id;
      link.href = '#';
      link.textContent = id;
      if (id ==='English' || id ==='Mandarin' || id ==='Cantonese' || id==='Punjabi') {
        link.className = 'active';
      } else { link.className = '';}
    
   
      link.onclick = function (e) {
        const clickedLayer = this.textContent;
        e.preventDefault();
        e.stopPropagation();
    
      const visibility = map.getLayoutProperty(
        clickedLayer,
        'visibility'
      );
    
  
      if (visibility === 'visible') {
        map.setLayoutProperty(clickedLayer, 'visibility', 'none');
        this.className = '';
      } else {
        this.className = 'active';
        map.setLayoutProperty(
          clickedLayer,
          'visibility',
          'visible'
        );
      }
    };
    
    const layers = document.getElementById('menu');
    layers.appendChild(link);

    if (id == 'Arabic'){
    document.getElementById("color1").style.fill = '#fb9a99'
    var img = document.getElementById("circle1");
    var newimg = img.cloneNode(true);
    link.appendChild(newimg);
    }

    if (id == 'Bengali'){
    document.getElementById("color1").style.fill = '#edf907'
    var img = document.getElementById("circle1");
    var newimg2 = img.cloneNode(true);
    link.appendChild(newimg2);
    }

    if (id == 'Cantonese'){
    document.getElementById("color1").style.fill = '#2b13ff'
    var img = document.getElementById("circle1");
    var newimg3 = img.cloneNode(true);
    link.appendChild(newimg3);
    }

    if (id == 'Croatian'){
    document.getElementById("color1").style.fill = '#af8080'
    var img = document.getElementById("circle1");
    var newimg4 = img.cloneNode(true);
    link.appendChild(newimg4);
    }

    if (id == 'Dari'){
    document.getElementById("color1").style.fill = '#cc67bd'
    var img = document.getElementById("circle1");
    var newimg5 = img.cloneNode(true);
    link.appendChild(newimg5);
    }

    if (id == 'English'){
    document.getElementById("color1").style.fill = '#FFCCCB'
    var img = document.getElementById("circle1");
    var newimg6 = img.cloneNode(true);
    link.appendChild(newimg6);
    }

    if (id == 'French'){
    document.getElementById("color1").style.fill = '#ad7400'
    var img = document.getElementById("circle1");
    var newimg7 = img.cloneNode(true);
    link.appendChild(newimg7);
    }

    if (id == 'German'){
    document.getElementById("color1").style.fill = '#000000'
    var img = document.getElementById("circle1");
    var newimg8 = img.cloneNode(true);
    link.appendChild(newimg8);
    }

    if (id == 'Greek'){
    document.getElementById("color1").style.fill = '#5abde8'
    var img = document.getElementById("circle1");
    var newimg9 = img.cloneNode(true);
    link.appendChild(newimg9);
    }

    if (id == 'Gujarati'){
    document.getElementById("color1").style.fill = '#ceb25d'
    var img = document.getElementById("circle1");
    var newimg10 = img.cloneNode(true);
    link.appendChild(newimg10);
    }

    if (id == 'Hindi'){
    document.getElementById("color1").style.fill = '#6a6a6a'
    var img = document.getElementById("circle1");
    var newimg11 = img.cloneNode(true);
    link.appendChild(newimg11);
    }

    if (id == 'Hungarian'){
    document.getElementById("color1").style.fill = '#176426'
    var img = document.getElementById("circle1");
    var newimg12 = img.cloneNode(true);
    link.appendChild(newimg12);
    }

    if (id == 'Iranian-Persian'){
    document.getElementById("color1").style.fill = '#fdbf6f'
    var img = document.getElementById("circle1");
    var newimg13 = img.cloneNode(true);
    link.appendChild(newimg13);
    }

    if (id == 'Italian'){
    document.getElementById("color1").style.fill = '#00fff7'
    var img = document.getElementById("circle1");
    var newimg14 = img.cloneNode(true);
    link.appendChild(newimg14);
    }

    if (id == 'Korean'){
    document.getElementById("color1").style.fill = '#d400ff'
    var img = document.getElementById("circle1");
    var newimg15 = img.cloneNode(true);
    link.appendChild(newimg15);
    }

    if (id == 'Malayalam'){
    document.getElementById("color1").style.fill = '#8cff00'
    var img = document.getElementById("circle1");
    var newimg16 = img.cloneNode(true);
    link.appendChild(newimg16);
    }

    if (id == 'Mandarin'){
    document.getElementById("color1").style.fill = '#ff0000'
    var img = document.getElementById("circle1");
    var newimg17 = img.cloneNode(true);
    link.appendChild(newimg17);
    }

    if (id == 'Other'){
    document.getElementById("color1").style.fill = "#b2df8a"
    var img = document.getElementById("circle1");
    var newimg18 = img.cloneNode(true);
    link.appendChild(newimg18);
    }

    if (id == 'Polish'){
    document.getElementById("color1").style.fill = '#cbb5ff'
    var img = document.getElementById("circle1");
    var newimg19 = img.cloneNode(true);
    link.appendChild(newimg19);
    }

    if (id == 'Portuguese'){
    document.getElementById("color1").style.fill = '#33a02c'
    var img = document.getElementById("circle1");
    var newimg20 = img.cloneNode(true);
    link.appendChild(newimg20);
    }

    if (id == 'Punjabi'){
    document.getElementById("color1").style.fill = '#7f6646'
    var img = document.getElementById("circle1");
    var newimg21 = img.cloneNode(true);
    link.appendChild(newimg21);
    }

    if (id == 'Romanian'){
    document.getElementById("color1").style.fill = '#ffffff'
    var img = document.getElementById("circle1");
    var newimg22 = img.cloneNode(true);
    link.appendChild(newimg22);
    }

    if (id == 'Russian'){
    document.getElementById("color1").style.fill = '#034493'
    var img = document.getElementById("circle1");
    var newimg23 = img.cloneNode(true);
    link.appendChild(newimg23);
    }

    if (id == 'Serbian'){
    document.getElementById("color1").style.fill = '#720808'
    var img = document.getElementById("circle1");
    var newimg24 = img.cloneNode(true);
    link.appendChild(newimg24);
    }

    if (id == 'Spanish'){
    document.getElementById("color1").style.fill = '#ff7f00'
    var img = document.getElementById("circle1");
    var newimg25 = img.cloneNode(true);
    link.appendChild(newimg25);
    }

    if (id == 'Tagalog'){
    document.getElementById("color1").style.fill = '#7b71f7'
    var img = document.getElementById("circle1");
    var newimg26 = img.cloneNode(true);
    link.appendChild(newimg26);
    }

    if (id == 'Tamil'){
    document.getElementById("color1").style.fill = '#ffee00'
    var img = document.getElementById("circle1");
    var newimg27 = img.cloneNode(true);
    link.appendChild(newimg27);
    }

    if (id == 'Telugu'){
    document.getElementById("color1").style.fill = '#cdc9ff'
    var img = document.getElementById("circle1");
    var newimg28 = img.cloneNode(true);
    link.appendChild(newimg28);
    }

    if (id == 'Turkish'){
    document.getElementById("color1").style.fill = '#7393B3'
    var img = document.getElementById("circle1");
    var newimg29 = img.cloneNode(true);
    link.appendChild(newimg29);
    }

    if (id == 'Ukrainian'){
    document.getElementById("color1").style.fill = '#ffc800'
    var img = document.getElementById("circle1");
    var newimg30 = img.cloneNode(true);
    link.appendChild(newimg30);
    }

    if (id == 'Urdu'){
    document.getElementById("color1").style.fill = '#1f78b4'
    var img = document.getElementById("circle1");
    var newimg31 = img.cloneNode(true);
    link.appendChild(newimg31);
    }

    if (id == 'Vietnamese'){
    document.getElementById("color1").style.fill = '#8b34be'
    var img = document.getElementById("circle1");
    var newimg32 = img.cloneNode(true);
    link.appendChild(newimg32);
    }


  }
  });




  
  });
  
</script>


<head>
<meta charset="utf-8">
<title>Load data from an external GeoJSON file</title>
<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
//<link href="https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css" rel="stylesheet">
//<script src="https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.js"></script>
<svg id="circle1" height="20" width="20">
    <circle id="color1" cx="10" cy="10" r="8" stroke="black" stroke-width="0.5" fill="#ffffff" />
</svg>
<style>
body { margin: 0; padding: 0; }
#map { position: fixed; top: 0; bottom: 0; right: 0; left: 0; width: 100%; }
.mapboxgl-popup {
  max-width: 400px;
  font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
  width: 180px;
}
.map-overlay {
  position: absolute;
  bottom: 0;
  right: 0;
  background: #fff;
  margin-right: 20px;
  font-family: Arial, sans-serif;
  overflow: auto;
  border-radius: 3px;
}
</style>
</head>

<body>
<style>
  #menu {
    background: #BEBDB8;
    position: absolute;
    z-index: 1;
    top: 10px;
    right: 10px;
    border-radius: 3px;
    width: 120px;
    border: 1px solid rgba(0, 0, 0, 0.4);
    font-family: 'Open Sans', sans-serif;
  }
  
  #menu a {
    font-size: 10px;
    color: #404040;
    display: block;
    margin: 0;
    padding: 0;
    padding: 5px;
    text-decoration: none;
    border-bottom: 1px solid rgba(0, 0, 0, 0.25);
    text-align: center;
  }
  
  #menu a:last-child {
    border: none;
  }
  
  #menu a:hover {
    background-color: #f8f8f8;
    color: #404040;
  }
  
  #menu a.active {
    background-color: #D9DDDC;
    color: #000000;
  }
  
  #menu a.active:hover {
    background: #BEBDB8;
  }

  #legend {
    padding: 10px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    line-height: 18px;
    height: 150px;
    margin-bottom: 40px;
    margin-right: 1000px;
    width: 300px;
  }

  .legend-key {
    display: inline-block;
    border-radius: 20%;
    width: 10px;
    height: 10px;
    margin-right: 5px;
  }

</style>
  
<nav id="menu">
</nav>





<div id="map">
</div>

<div class='map-overlay' id='legend'></div>
 
</body>
