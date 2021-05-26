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
    <el-table
      v-loading="listLoading"
      :data="list"
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
      <!-- <el-table-column class-name="status-col" label="描述" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter" >{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column> -->
      <!-- <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column> -->
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/hots'

export default {
  // filters: {
  //   statusFilter(status) {
  //     const statusMap = {
  //       published: 'success',
  //       draft: 'gray',
  //       deleted: 'danger'
  //     }
  //     return statusMap[status]
  //   }
  // },
  data() {
    return {
      list: null,
      listLoading: true,
      currentHotTime: null,
      count: 0,
      maxCount: 0,
      listQuery: {
        hot_type: "zhihu",
        count: -1,
      },
    }
  },
  created() {
    this.fetchData()
    setTimeout(() => {
    this.maxCount = this.count;
    }, 1000);
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList(this.listQuery ).then(response => {
        console.log(response)
        this.list = response.data.fields.hots
        this.currentHotTime = response.data.fields.time;
        this.count = response.data.fields.count;
        this.listLoading = false
      })
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
    tableRowClassName (row) {
      if (parseInt(row.row.ranking) <= 5) {
        return 'rowstyle';
      }
    }
  }
}
</script>

<style lang="scss">
  .el-tag {
  width: 100px;
}
.el-table .rowstyle {
  color: red;
}
</style>
