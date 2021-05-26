<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import * as echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme

export default {
  name: "linechart",
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '350px'
    },
    chartData: {
      xAxisData: Array,
      posData: Array,
      negData: Array,
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  // mounted() {
  //   this.$nextTick(() => {
  //     this.initChart()
  //   })
  // },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions(this.chartData)
    },
    setOptions() {
      this.chart.setOption({
         title: {
          text: '情感趋势',
          textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
            color: 'rgba(3,43,120)'
          },
          left: '1%'
        },
        xAxis: {
          data: this.chartData.xAxisData,
          boundaryGap: false,
          axisTick: {
            show: false
          }
        },
        grid: {
          left: 10,
          right: 10,
          bottom: 20,
          top: 30,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          },
          padding: [5, 10]
        },
        yAxis: {
          axisTick: {
            show: false
          }
        },
        legend: {
          data: ['Positive', 'Negative']
        },
        series: [{
          name: 'Positive', 
          itemStyle: {
              color: '#FF005A',
              lineStyle: {
                color: '#FF005A',
                width: 2
              }
          },
          smooth: true,
          type: 'line',
          data: this.chartData.posData,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        },
        {
          name: 'Negative',
          smooth: true,
          type: 'line',
          itemStyle: {
              color: '#3888fa',
              lineStyle: {
                color: '#3888fa',
                width: 2
              },
              areaStyle: {
                color: '#f3f8ff'
              }
          },
          data: this.chartData.negData,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }]
      })
    }
  }
}
</script>
