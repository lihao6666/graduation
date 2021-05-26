<template>
  <div class="app-container">
    <el-input
      v-model="addQuery.content"
      placeholder="输入添加内容"
      style="width: 200px; margin: 20px"
      class="filter-item"
      @keyup.enter.native="addSearchContent"
    />
    <el-button
      class="filter-item"
      style="margin-left: 10px"
      type="primary"
      icon="el-icon-edit"
      @click="addSearchContent"
    >
      Add
    </el-button>
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

      <el-table-column align="center" label="Content">
        <template slot-scope="{ row }">
          <span>{{ row.fields.search_content }}</span>
        </template>
      </el-table-column>

      <el-table-column width="70px" align="center" label="Patch">
        <template slot-scope="{ row }">
          <span>{{ row.fields.patch }}</span>
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="Type" width="110">
        <template slot-scope="{ row }">
          <el-tag style = "width:60px" type="row.fields.type | statusFilter">
            {{ row.fields.type }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Actions" width="120">
        <template slot-scope="{ row }">
          <el-button
            type="primary"
            size="small"
            :disabled="row.fields.patch == 0"
            icon="el-icon-circle-check-outline"
            @click="goDetail(row)"
            >详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getSearch,addSearch } from "@/api/chart";
import { mapMutations } from "vuex";

export default {
  name: "InlineEditTable",
  filters: {
    statusFilter(status) {
      const statusMap = {
        weibo: "success",
        zhihu: "info",
      };
      return statusMap[status];
    },
  },
  data() {
    return {
      list: null,
      listLoading: true,
      listQuery: {
        search_type: "weibo",
      },
      addQuery: {
        content: undefined,
        type: "weibo",
      },
    };
  },
  created() {
    this.getList();
  },
  methods: {
    ...mapMutations({
      addContent: "detail/ADD_CONTENT",
    }),
    async getList() {
      this.listLoading = true;

      const { data } = await getSearch(this.listQuery);
      this.list = data;
      this.listLoading = false;
    },

    goDetail(row) {
      this.addContent({
        content: row.fields.search_content,
        patch: row.fields.patch,
      });
      this.$router.push({
        name: "detail",
        query: {
          content: row.fields.search_content,
          patch: row.fields.patch,
        },
      });
      this.$message({
        message: "跳转成功",
        type: "success",
      });
    },
    async addSearchContent() {
      console.log(this.addQuery)
      const { data } = await addSearch(this.addQuery);
      if(data.signal == 0)
      {
        this.$message({
        message: "添加失败，队列中已经存在",
        type: "warning",
      });
      }
      else{
        this.getList()
        this.$message({
        message: "添加成功",
        type: "success",
      });
      }
    },
  },
};
</script>

<style scoped>
.edit-input {
  padding-right: 100px;
}
.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
</style>
