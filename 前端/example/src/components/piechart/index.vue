<template>
  <div :class="className" :style="{ height: height, width: width }" />
</template>

<script>
import * as echarts from "echarts";
require("echarts/theme/macarons"); // echarts theme

export default {
  name: "piechart",
  props: {
    className: {
      type: String,
      default: "chart",
    },
    width: {
      type: String,
      default: "380px",
    },
    height: {
      type: String,
      default: "300px",
    },
    dataList: Array,
  },
  data() {
    return {
      chart: null,
      legendData: null,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart();
    });
  },
  methods: {
    initChart() {

    if (this.chart != null && this.chart != "" && this.chart != undefined) {
        this.chart.dispose();
      }
      this.legendData = new Array()
      var j 
      for(j = 0; j < this.dataList.length; j++) {
          this.legendData.push(this.dataList[j]["name"])
        } 
        console.log(this.legendData)
      this.chart = echarts.init(this.$el, "macarons");

      this.chart.setOption({
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        legend: {
          left: "center",
          bottom: "10",
          data: this.legendData,
        },
        series: [
          {
            name: "情感分布",
            type: "pie",
            roseType: "radius",
            radius: [15, 80],
            center: ["50%", "38%"],
            data: this.dataList,
            animationEasing: "cubicInOut",
            animationDuration: 2600,
          },
        ],
      });
    },
  },
};
</script>
