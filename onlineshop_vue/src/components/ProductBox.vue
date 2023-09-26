<template>
  <div class="page-prod">
    <div class="card-container column is-2 mb-2 ml-3">
      <div class="card-image">
        <img v-bind:src="product.get_thumbnail">
      </div>
      <p class="is-size-5  text-title">{{ product.name }}</p>
      <p class="is-size-6 text-title card-content">{{ product.brand }}</p>
      <p class="is-size-6 has-text-grey card-content">{{ product.price }} руб.</p>
      <div class="card-footer">
        <router-link v-bind:to="product.get_absolute_url" class="button mt-4 is-orange text card-footer-item">Подробнее</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .card-container{
    margin-bottom: 3px;
    border-radius: 8px;
    border: thin solid #ff6b00;
    width: 220px;
    height: 400px;
    text-align: center;

  }
  .page-prod{
    margin-right: 2px;
  }
  .is-orange{
    background: #ff6b00;
    color: #FFFFFF;
  }
  .text{
    font-style: normal;
    font-weight: 700;
    text-transform: uppercase;
    color: #ffffff;
  }
  .text-title{
    font-style: normal;
    font-weight: 500;
    text-transform: uppercase;
    color: #000000;
  }
</style>