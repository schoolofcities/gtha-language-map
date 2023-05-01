<script>

export let languageTotalColours;
export let chartLanguages;

$: filteredData = languageTotalColours.filter(item => chartLanguages.includes(item.Language));

$: svgHeight = chartLanguages.length * 25;
$: svgWidth = 300;

let maxValue = 0;
let ratio = 0;

$: if (chartLanguages.length !== 0) {
    filteredData = filteredData.sort((a, b) => b.Speakers - a.Speakers);
    maxValue = filteredData[0]["Speakers"];
} else {
    maxValue = 0;
    ratio = 0;
}

$: console.log(filteredData);


</script>


<div id="chart">
    <p id="chartTitle">
        <b>Total Number of Speakers in the GTHA:</b>
    </p>
    <svg height="{svgHeight}" width={svgWidth} id="svgChart">
        {#each filteredData as d, i}
            <text 
                class="label" 
                x = "0" 
                y = {10 + i * 25}
            >{d["Language"]} - {d["Speakers"].toLocaleString()}</text>
            
            <line class="dataLine"
                x1 = "0"
                y1 = {14 + i * 25}
                x2 = {5 + svgWidth * d["Speakers"] / maxValue}
                y2 = {14 + i * 25}
                stroke ="{d.Colour}"
                stroke-width = "2"
            ></line>
            
        {/each}
    </svg>
</div>

<style>

    #chart {
        width: 300px;
        margin-left: 5px;
        padding: 5px;
        margin-bottom: 10px;
        border-top: solid 1px var(--brandGray);
    }

    #chartTitle {
        text-align: left;
        font-size: 13px;
    }

    #svgChart {
        background-color: none;
    }

   
    .label {
        margin: 0px;
        color: var(--brandDarkGray);
        font-weight: normal;
        line-height: 14px;
        font-size: 12px;
    }
    

</style>