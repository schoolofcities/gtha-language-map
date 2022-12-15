

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

      map.addSource("languages", {
      "type": "geojson",
      "data": "data/no_water_commercial_industrial.geojson"
      });

      //English 

       map.addLayer({
        "id": "English",
        "type": "circle",
        "source": "languages",
        "paint": {
        "circle-radius": ['sqrt', ['/', ['get', 'Speaker_No'], 10]],
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
      link.className = 'active';
    
   
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
    var img = document.createElement('img');
    img.src = "data/Arabic.png"
    link.appendChild(img);
    }

    if (id == 'Bengali'){
    var img = document.createElement('img');
    img.src = "data/Bengali.png"
    link.appendChild(img);
    }

    if (id == 'Cantonese'){
    var img = document.createElement('img');
    img.src = "data/Cantonese.png"
    link.appendChild(img);
    }

    if (id == 'Croatian'){
    var img = document.createElement('img');
    img.src = "data/Croatian.png"
    link.appendChild(img);
    }

    if (id == 'Dari'){
    var img = document.createElement('img');
    img.src = "data/Dari.png"
    link.appendChild(img);
    }

    if (id == 'English'){
    var img = document.createElement('img');
    img.src = "data/English.png"
    link.appendChild(img);
    }

    if (id == 'French'){
    var img = document.createElement('img');
    img.src = "data/French.png"
    link.appendChild(img);
    }

    if (id == 'German'){
    var img = document.createElement('img');
    img.src = "data/German.png"
    link.appendChild(img);
    }

    if (id == 'Greek'){
    var img = document.createElement('img');
    img.src = "data/Greek.png"
    link.appendChild(img);
    }

    if (id == 'Gujarati'){
    var img = document.createElement('img');
    img.src = "data/Gujarati.png"
    link.appendChild(img);
    }

    if (id == 'Hindi'){
    var img = document.createElement('img');
    img.src = "data/Hindi.png"
    link.appendChild(img);
    }

    if (id == 'Hungarian'){
    var img = document.createElement('img');
    img.src = "data/Hungarian.png"
    link.appendChild(img);
    }

    if (id == 'Iranian-Persian'){
    var img = document.createElement('img');
    img.src = "data/Iranian_Persian.png"
    link.appendChild(img);
    }

    if (id == 'Italian'){
    var img = document.createElement('img');
    img.src = "data/Italian.png"
    link.appendChild(img);
    }

    if (id == 'Korean'){
    var img = document.createElement('img');
    img.src = "data/Korean.png"
    link.appendChild(img);
    }

    if (id == 'Malayalam'){
    var img = document.createElement('img');
    img.src = "data/Malayalam.png"
    link.appendChild(img);
    }

    if (id == 'Mandarin'){
    var img = document.createElement('img');
    img.src = "data/Mandarin.png"
    link.appendChild(img);
    }

    if (id == 'Other'){
    var img = document.createElement('img');
    img.src = "data/Other.png"
    link.appendChild(img);
    }

    if (id == 'Polish'){
    var img = document.createElement('img');
    img.src = "data/Polish.png"
    link.appendChild(img);
    }

    if (id == 'Portuguese'){
    var img = document.createElement('img');
    img.src = "data/Portuguese.png"
    link.appendChild(img);
    }

    if (id == 'Punjabi'){
    var img = document.createElement('img');
    img.src = "data/Punjabi.png"
    link.appendChild(img);
    }

    if (id == 'Romanian'){
    var img = document.createElement('img');
    img.src = "data/Romanian.png"
    link.appendChild(img);
    }

    if (id == 'Russian'){
    var img = document.createElement('img');
    img.src = "data/Russian.png"
    link.appendChild(img);
    }

    if (id == 'Serbian'){
    var img = document.createElement('img');
    img.src = "data/Serbian.png"
    link.appendChild(img);
    }

    if (id == 'Spanish'){
    var img = document.createElement('img');
    img.src = "data/Spanish.png"
    link.appendChild(img);
    }

    if (id == 'Tagalog'){
    var img = document.createElement('img');
    img.src = "data/Tagalog.png"
    link.appendChild(img);
    }

     if (id == 'Tamil'){
    var img = document.createElement('img');
    img.src = "data/Tamil.png"
    link.appendChild(img);
    }

    if (id == 'Telugu'){
    var img = document.createElement('img');
    img.src = "data/Telugu.png"
    link.appendChild(img);
    }

    if (id == 'Turkish'){
    var img = document.createElement('img');
    img.src = "data/Turkish.png"
    link.appendChild(img);
    }

    if (id == 'Ukrainian'){
    var img = document.createElement('img');
    img.src = "data/Ukrainian.png"
    link.appendChild(img);
    }

    if (id == 'Urdu'){
    var img = document.createElement('img');
    img.src = "data/Urdu.png"
    link.appendChild(img);
    }

    if (id == 'Vietnamese'){
    var img = document.createElement('img');
    img.src = "data/Vietnamese.png"
    link.appendChild(img);
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
<style>
body { margin: 0; padding: 0; }
#map { position: fixed; top: 0; bottom: 0; right: 0; left: 0; width: 100%; }
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
    //3887be, ffffff
  }
  
  #menu a.active:hover {
    background: #BEBDB8;
    //#3074a4
  }
</style>
  
<nav id="menu">
</nav>

<div id="map">
</div>
 
</body>
