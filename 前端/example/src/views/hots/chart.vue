<template>
  <div class="chart-container">
    <chart ref = "chart" :dataList="dataList" height="100%" width="100%" />
  </div>
</template>

<script>
import Chart from '@/components/Charts/LineMarker'
import { getHotsChange } from "@/api/hots";

export default {
  name: 'LineChart',
  components: { Chart },
  data() {
    return {
     dataList: null,
    };
  },
  mounted() {
    this.getList();
  },
  methods: {
    getList() {
    this.listLoading = true;
    const param = this.$route.query;
    getHotsChange({ date:param.date}).then((response) => {
    this.dataList = response.data
    setTimeout(() => {
        this.$refs.chart.initChart()
      }, 10);
    })
  }
}
}
</script>
<style>
.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
}
</style>

