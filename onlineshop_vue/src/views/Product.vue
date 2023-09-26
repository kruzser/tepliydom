<template>
  <h1 class="title">{{ product.name }}</h1>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="columns is-9">
        <figure class="image mb-6">
          <img v-bind:src="product.get_image">
        </figure>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Характеристик</h2>
        <p><strong>Цена: </strong>{{ product.price }} руб.</p>
        <p><strong>Бренд: </strong>{{ product.brand }}</p>
        <div class="field has-addons mt-6">
          <div class="control mr-1">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>
          <div class="control">
            <a class="button is-dark" @click="addToCart()">Добавить корзину</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="mb-5 mt-5">
    <h2 class="subtitle">Описание</h2>
     <p>{{ product.description }}</p>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'
export default {
  name: 'Product',
  data() {
    return {
      product: {},
      quantity: 1
    }
  },
  mounted() {
    this.getProduct()
  },
  methods: {
    async getProduct() {
      this.$store.commit('setIsLoading', true)

      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

      await axios
          .get(`/api/v1/products/${category_slug}/${product_slug}`)
          .then(responce => {
            this.product = responce.data

            document.title = this.product.name + '- характеристики | Магазин штук'
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity <1) {
        this.quantity = 1
      }

      const item = {
        product: this.product,
        quantity: this.quantity
      }

      this.$store.commit('addToCart', item)

      toast({
        message: 'Товар добавлен в корзину',
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right'
      })

    }
  }
}
</script>
<style>
.page-product{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>