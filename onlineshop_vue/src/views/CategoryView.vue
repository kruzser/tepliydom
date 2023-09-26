<template>
  <div class="mb-6 home-text-black is-size-3">{{ category.name }}</div>
  <div class="page-category">
    <div class="category-container">
      <div class="filter-bar pr-2 " v-if="filters.length > 0">
        <h2 class="is-size-5 home-text">{{ category.name }}</h2>
        <div v-if="category.total > 1" class="pagination home-text">
          Страницы:
          <div v-for="index in category.total" :key="index">
            <button class="is-dark pagination-button ml-1" v-on:click="getCategoryPage(index)">{{index}}</button>
          </div>
        </div>
        <div v-for="filter_obj in filters">
          <h3 class="home-text">{{filter_obj.name}}</h3>
          <div v-if="filter_obj.slug === 'price'" class="home-price">
            <input v-model="min_price" class="price-input" placeholder="Минимальная цена">
            <input v-model="max_price" class="price-input" placeholder="Максимальная цена">
          </div>
          <div v-if="filter_obj.slug === 'brand'">
            <div v-for="brand in brands" class="home-text-black">
              <input type="checkbox" id="{{brand.brand}}" v-model="choosedBrands" v-bind:value="brand.brand">
              <label class="ml-2" for="{{brand.brand}}">{{brand.brand}} ({{brand.total}})</label>
            </div>
          </div>
        </div>
        <button class="home-register mr-2 ml-2 button home-text" v-on:click="getCategoryPage(this.page)">Применить</button>
      </div>
      <div class="card-bar columns is-multiline" v-if="category.total !== 0">
        <ProductBox
            v-for="product in category.products"
            v-bind:key="product.id"
            v-bind:product="product"
        />
      </div>
      <div v-else >
        <router-link to="/"><span class="home-text-title ml-6">Тут пока пусто... Вернитесь в каталог</span></router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox'
export default {
  name: 'Category',
  components: {
    ProductBox
  },
  data() {
    return {
      min_price:0,
      max_price:1000000,
      choosedBrands: [],
      filters: [],
      brands: [],
      page: 1,
      category: {
        products: []
      }
    }
  },
  mounted() {
    this.getFilters()
    this.getCategoryPage(1)
    this.getBrand()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Category') {
        this.getCategoryPage()
      }
    }
  },
  methods: {
    async getFilters(){
      const categorySlug = this.$route.params.category_slug
      axios
        .get(`/api/v1/filters/${categorySlug}`)
        .then(responce => {
          this.filters = responce.data
        })
        .catch(error => {
          console.log(error)
          toast({
            message: 'Чтот-то пошло не так. Попробуйте снова.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
    },
    async getCategoryPage(index) {
      this.page = index
      const categorySlug = this.$route.params.category_slug
      this.$store.commit('setIsLoading', true)
      axios
        .post(`/api/v1/products/${categorySlug}/9/`+(this.page-1), {"filters": [
          {"price": {
              "max_price": this.max_price,
              "min_price": this.min_price
          }},
          {"brands": this.choosedBrands}
          ]}
        )
        .then(response => {
          this.category = response.data
          document.title = this.category.name + '| Теплый дом'
        })
        .catch(error => {
          console.log(error)
          toast({
            message: 'Чтот-то пошло не так. Попробуйте снова.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
      this.$store.commit('setIsLoading', false)
    },
    async getBrand(){
      axios
        .get(`/api/v1/get_brands/`)
        .then(responce => {
          this.brands = responce.data
        })
        .catch(error => {
          console.log(error)
          toast({
            message: 'Чтот-то пошло не так. Попробуйте снова.',
            type: 'is-danger',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
    }
  }
}
</script>
<style>
.category-container{
  display: flex;
}
.filter-bar{
  display: flex;
  border-right: thick solid #ff6b00;
  text-align: center;
  flex-direction: column;
  margin-left: 20px;
  padding-right: 20px !important;
}
.card-bar{
  margin-left: 2px;
  max-width: 1050px;
  display: block;
}
.pagination{
  margin: 15px 5px 5px;
}
.page-category{
  width: 100%;
  max-width: 1024px;
  display: flex;
  justify-content: flex-start;
}
.home-price{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.price-input{
  border: 1px solid #ff6b00;
  margin-left: 5px;
  width: 80px;
}
</style>