<template>
  <div class="app-container">
    <el-tag style="width: 180px; margin: 10px"
      >时间:{{ currentHotTime }}</el-tag
    >
    <el-button type="primary" size="small" @click="beforeHot()"
      >上一个</el-button
    >
    <el-button type="primary" size="small" @click="afterHot()"
      >下一个</el-button
    >
    <el-button type="success" size="small" @click="goChart()"
      >可视化</el-button
    >

    <el-table
      v-loading="listLoading"
      :data="list.slice((page - 1) * limit, page * limit)"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      :row-class-name="tableRowClassName"
    >
      <el-table-column align="center" label="排行" width="95">
        <template slot-scope="scope">
          {{ scope.row.ranking }}
        </template>
      </el-table-column>
      <el-table-column label="内容">
        <template slot-scope="scope">
          {{ scope.row.content }}
        </template>
      </el-table-column>
      <el-table-column label="热度" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.count }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column label="描述" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.pageviews }}
        </template>
      </el-table-column> -->
      <el-table-column
        class-name="status-col"
        label="描述"
        width="110"
        align="center"
      >
        <template slot-scope="scope">
          <el-tag style="width: 70px;" :type="scope.row.desc | statusFilter" class="desc">{{
            scope.row.desc
          }}</el-tag>
        </template>
      </el-table-column>

      <!-- <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column> -->
    </el-table>
    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="page"
      :limit.sync="limit"
      @pagination="getPaginationData"
    />
  </div>
</template>

<script>
import { getList } from "@/api/hots";
import Pagination from "@/components/Pagination";

export default {
  components: { Pagination },
  filters: {
    statusFilter(status) {
      const statusMap = {
        沸: "danger",
        热: "danger",
        新: "primary",
        荐: "success",
        None: "info",
      };
      return statusMap[status];
    },
  },
  data() {
    return {
      list: null,
      templist: null,
      listOrigin: null,
      listLoading: true,
      currentHotTime: null,
      count: 0,
      maxCount: 0,
      total: 0,
      page: 1000,
      limit: 10,
      listQuery: {
        hot_type: "weibo",
        count: -1,
      },
    };
  },
  created() {
    this.fetchData();
    setTimeout(() => {
      this.maxCount = this.count;
    }, 1000);
  },
  methods: {
    fetchData() {
      this.listLoading = true;
      getList(this.listQuery).then((response) => {
        this.list = response.data.fields.hots;
        this.currentHotTime = response.data.fields.time;
        this.count = response.data.fields.count;
        this.page = 1;
        this.total = 50;
        this.listLoading = false;
      });
    },
    beforeHot() {
      if (this.count - 1 < 1) {
        this.$message({
          message: "已经是最老的了亲",
          type: "warning",
        });
      } else {
        this.listQuery["count"] = this.count - 1;
        this.fetchData();
      }
    },
    afterHot() {
      console.log(this.count);
      console.log(this.maxCount);
      if (this.count + 1 > this.maxCount) {
        this.$message({
          message: "已经是最新的了亲",
          type: "warning",
        });
      } else {
        this.listQuery["count"] = this.count + 1;
        this.fetchData();
      }
    },
    goChart(){
      this.$router.push({
        name: "hotChart",
        query: {
          date: this.currentHotTime.slice(0,10)
        },
      });

    },
    tableRowClassName(row) {
      if (parseInt(row.row.ranking) <= 5) {
        return "rowstyle";
      }
    },
    getPaginationData(val) {
      this.page = val.page;
      this.limit = val.limit;
    },
  },
};
</script>


<style lang="scss">
.el-table .rowstyle {
  color: red;
}
</style>
