<template>
  <div class="app-container">
    <el-tag style="width: 220px; margin: 10px"
      >最新分析时间:{{ currentSearchTime }}</el-tag>
    <el-select v-model="currentPatch" style="width: 80px" class="patch-item" @change="changePatch">
        <el-option v-for="item in selectPatchs" :key="item" :label="item" :value="item" />
    </el-select>
    <el-table
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="序号" width="80">
        <template slot-scope="scope">
          <span>{{ scope.$index + 1 }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="mid" width="100px">
        <template slot-scope="{ row }">
          <span>{{ row.mid }}</span>
        </template>
      </el-table-column>

      <el-table-column  width="500px" show-overflow-tooltip align="center" label="微博内容">
        <template slot-scope="{ row }">
          <span>{{ row.content }}</span>
        </template>
      </el-table-column>

      <el-table-column width="70px" align="center" label="评论数">
        <template slot-scope="{ row }">
          <span>{{ row.comments_count }}</span>
        </template>
      </el-table-column>

      <!-- <el-table-column class-name="status-col" label="Type" width="110">
        <template slot-scope="{ row }">
          <el-tag :type="row.fields.type | statusFilter">
            {{ row.fields.type }}
          </el-tag>
        </template>
      </el-table-column> -->

      <el-table-column align="center" label="Actions" >
        <template slot-scope="{ row }">
          <el-button
            type="success"
            size="small"
            icon="el-icon-circle-check-outline"
            @click="goCloudChart(row)"
            >词云图 
          </el-button>
           <el-button
            type="primary"
            size="small"
            icon="el-icon-circle-check-outline"
            @click="goSpiritChart(row)"
            >情感图
          </el-button>
          <el-button
            type="info"
            size="small"
            icon="el-icon-circle-check-outline"
            @click="goLineChart(row)"
            >情感演变
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div style="background:#fff;margin-top:20px;margin-bottom:32px;">
      <line-chart ref = "linechart" :visible.sync="lineChartVisible" :chartData="lineChartData" />
    </div>
    <el-dialog
        :title="cloudChartName"
        :visible.sync="cloudChartVisible"
        width="30%"
      >
        <wordcloud ref = "wordcloud" :wordList = "currentResCount"></wordcloud>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="cloudChartVisible = false"
            >取消</el-button>
        </span>
      </el-dialog>

      <el-dialog
        :title="spiritChartName"
        :visible.sync="spiritChartVisible"
        width="30%"
      >
        <piechart ref = "piechart" :dataList = "currentResSpirit"></piechart>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="spiritChartVisible = false"
            >取消</el-button>
        </span>
      </el-dialog>
  </div>
</template>
<script>

import wordcloud from "@/components/wordcloud";
import piechart from "@/components/piechart";
import LineChart from '@/components/Charts/LineChart'

import { getDetail, getDetailChange } from "@/api/chart";
import { mapState, mapMutations } from "vuex";

export default {
  name: "InlineEditTable",
  components: { wordcloud,piechart,LineChart},
  filters: {
    statusFilter(status) {
      const statusMap = {
        weibo: "success",
        zhihu: "info",
      };
      return statusMap[status];
    },
  },
  computed: {
    ...mapState({
      content: (state) => state.detail.content,
      patch: (state) => state.detail.patch,
    }),
  },
  data() {
    return {
      list: null,
      listLoading: true,
      cloudChartVisible: false,
      spiritChartVisible: false,
      lineChartVisible: false,
      cloudChartName: "词云图",
      spiritChartName: "情感分析图",
      currentResCount: null,
      currentResSpirit: null,
      currentContent: null,
      currentPatch: 0,
      currentSearchTime: null,
      selectPatchs: null,
      lineChartData: null,
    };
  },
  created() {
    this.getList();
  },
  methods: {
    ...mapMutations({
      addRes: "detail/ADD_RES",
    }),
    async getList() {
      this.listLoading = true;
      const param = this.$route.query;
      const { data } = await getDetail({
        content: param.content,
        patch: param.patch,
        detail_type: "weibo",
      });
      this.currentSearchTime = data.parse_time
      this.currentContent = data.search_content
      this.currentPatch = data.search_patch
      this.selectPatchs = new Array()
      for(var i=1;i<=data.max_patch;i++)
      {
        this.selectPatchs.push(i)
      }
      this.addRes(data);
      this.list = data.weibos;
      this.listLoading = false;
    },

    goCloudChart(row) {
      this.currentResCount = row.res_count
      setTimeout(() => {
        this.$refs.wordcloud.initChart()
      }, 10);
      this.cloudChartVisible = true
    },
    goSpiritChart(row) {
      var res = new Array()
      for(var key in row.res_spirit)
      {
        var item = {}
        item["name"] = key
        item["value"] = row.res_spirit[key] 
        res.push(item)
      }
      this.currentResSpirit = res
      setTimeout(() => {
        this.$refs.piechart.initChart()
      }, 10);
      this.spiritChartVisible = true
    },
    goLineChart(row){
      const param = this.$route.query;
      getDetailChange({"content":param.content,"time": this.currentSearchTime, "mid": row.mid}).then((response) => {
      this.lineChartData = response.data
      setTimeout(() => {
        this.$refs.linechart.initChart()
      }, 10);
      })
    },
    changePatch(patch) {
      this.$router.push({
        name: "detail",
        query: {
          content: this.currentContent ,
          patch: patch,
        },
      });
      this.getList()

    }

  },
};
</script>

<style scoped>
</style>
