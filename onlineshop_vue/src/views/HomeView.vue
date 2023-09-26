<template>
  <div class="home home-container">
    <div class="columns level is-multiline mb-6 mt-2 category-list">
      <div v-for="category in categories">
        <router-link v-bind:to="category.get_absolute_url" class="home-text-black">
          {{category.name}}
        </router-link>
      </div>
    </div>
    <div class="pagination home-text ml-2">
      Страницы:
      <div v-for="index in cards.total" :key="index">
        <button class="is-dark ml-1 pagination-button" v-on:click="getPage(index)">{{index}}</button>
      </div>
    </div>
    <div class="columns is-multiline flex-container products-list">
      <ProductBox
        v-for="product in cards.products"
        v-bind:key="product.id"
        v-bind:product="product"
        class="is-flex-grow-1"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from '@/components/ProductBox'
export default {
  name: 'HomeView',
  data(){
    return{
      categories: [],
      cards:{products: []},
      page: 1
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getCategory()
    this.getPage(1)
    document.title = "Главная | Теплый дом"
  },
  methods:{
    async getPage(index) {
      this.page = index-1
      this.$store.commit('setIsLoading', true)
      await axios
       .get('/api/v1/latest-products/9/'+(this.page))
       .then(response => {
         this.cards = response.data
       })
       .catch(error => {
         console.log(error)
       })
      this.$store.commit('setIsLoading', false)
    },
    async getCategory() {
      await axios
       .get('/api/v1/category')
       .then(response => {
         this.categories = response.data
       })
       .catch(error => {
         console.log(error)
       })
    }


  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .category-list{
    width: 80%;
  }
  .products-list{
    padding-right: 4px;
    padding-left: 2px;
    padding-bottom: 5%;
  }
</style>
