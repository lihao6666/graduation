<template>
  <div :id="id" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import * as echarts from "echarts";
// import {resize} from './mixins/resize'

export default {
  // mixins: [resize],
  name: "chart",
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '200px'
    },
    height: {
      type: String,
      default: '200px'
    },
    dataList: {
      xAxisList: Array,
      Top1List: Array,
      Top2List: Array,
      Top3List: Array,
      Descs: Array,
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    // this.initChart()
    window.preventShake = true
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      window.desc = this.dataList.Descs
      this.chart = echarts.init(document.getElementById(this.id))
      this.chart.setOption({
        backgroundColor: '#394056',
        title: {
          top: 20,
          text: '热点趋势',
          textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
            color: '#F1F1F3'
          },
          left: '1%'
        },
        tooltip: {
          
          trigger: 'axis',
          formatter: function (params) {
            if (!window.preventShake) {
              return
            }
            window.preventShake = false
            setTimeout(() => {
              window.preventShake = true
            }, 200)
            var res = params[0].name+'<br/>'
            for(var i=0;i<params.length;i++)
            {
              var index = params[i].dataIndex
              var desc = window.desc[i][index]
              res +=params[i].marker+" "+ desc+": "+params[i].value+'<br/>'
            }
            return res
          },
          axisPointer: {
            lineStyle: {
              color: '#57617B'
            }
          }
        },
        legend: {
          top: 20,
          icon: 'rect',
          itemWidth: 14,
          itemHeight: 5,
          itemGap: 13,
          data: ['Top1', 'Top2', 'Top3'],
          right: '4%',
          textStyle: {
            fontSize: 12,
            color: '#F1F1F3'
          }
        },
        grid: {
          top: 100,
          left: '2%',
          right: '2%',
          bottom: '2%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: '#57617B'
            }
          },
          data: this.dataList.xAxisList
        }],
        yAxis: [{
          type: 'value',
          name: '热度',
          axisTick: {
            show: false
          },
          axisLine: {
            lineStyle: {
              color: '#57617B'
            }
          },
          axisLabel: {
            margin: 10,
            fontSize: 14
          },
          splitLine: {
            lineStyle: {
              color: '#57617B'
            }
          }
        }],
        series: [{
          name: 'Top1',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
              width: 1
          },
          areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(219, 50, 51, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(219, 50, 51, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
          },
          itemStyle: {
              color: 'rgb(219,50,51)',
              borderColor: 'rgba(219,50,51,0.2)',
              borderWidth: 12
          },
          data: this.dataList.Top1List
        }, {
          name: 'Top2',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
              width: 1
          },
          areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 136, 212, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(0, 136, 212, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
          },
          itemStyle: {
              color: 'rgb(0,136,212)',
              borderColor: 'rgba(0,136,212,0.2)',
              borderWidth: 12

          },
          data: this.dataList.Top2List
        }, {
          name: 'Top3',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
              width: 1
          },
          areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(137, 189, 27, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(137, 189, 27, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
          },
          itemStyle: {
              color: 'rgb(137,189,27)',
              borderColor: 'rgba(137,189,2,0.27)',
              borderWidth: 12
          },
          data: this.dataList.Top3List
        }]
      })

      this.chart.on('hover', (args) => {
        console.log(args)
      })
    }
  }
}
</script>
