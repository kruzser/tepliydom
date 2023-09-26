<template>
  <div id="wrapper">
    <div class="home-container">
      <header data-thq="thq-navbar" class="home-navbar-interactive">
        <div data-thq="thq-navbar-nav" class="home-desktop-menu">
          <div class="home-container1">
            <div class="home-container2">
              <div class="home-container3">
                <button class="home-register mr-2 ml-2 button mobile-view">
                  <template v-if="$store.state.isAuthenticated">
                    <router-link to="/account" class="home-text">Личный кабинет</router-link>
                  </template>
                  <template v-else>
                    <router-link to="/log-in" class="home-text" >Войти</router-link>
                  </template>
                </button>
                <div class="home-container4">
                  <router-link to="/" class="home-register mr-2 ml-2 button mobile-hide">
                    <span class="home-text">
                      <span>О нас</span>
                      <br />
                    </span>
                  </router-link>
                  <router-link to="/" class="home-register mr-2 ml-2 button mobile-hide">
                    <span class="home-text">
                      <span>Монтаж</span>
                      <br />
                    </span>
                  </router-link>
                </div>
                <router-link to="/" class="home-register2 mr-2 mt-2 button">
                  <img src=".\assets\category.svg" alt="">
                  <span class="home-text-category">
                    <span>Каталог</span>
                    <br />
                  </span>
                </router-link>
              </div>
              <div class="home-container5">
                <router-link to="/" class="home-text-title home-button">Теплый Дом</router-link>
                <form method="get" action="/search">
                  <div class="home-search">
                    <input type="text" placeholder="Введите название товара" name="query" class="home-textinput input">
                    <button class="home-register2 button search-button">
                        <i class="fas fa-search"></i>
                    </button>
                  </div>
                </form>
              </div>
              <div class="home-container3">
                <div class="home-container4">
                  <button class="home-register mr-2 ml-2 button mobile-hide">
                    <template v-if="$store.state.isAuthenticated">
                      <router-link to="/account" class="home-text">Личный кабинет</router-link>
                    </template>
                    <template v-else>
                      <router-link to="/log-in" class="home-text" >Войти</router-link>
                    </template>
                  </button>
                  <router-link to="/cart" class="home-register mr-2 ml-2 button shopping-cart">
                    <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                    <span class="home-text mobile-hide">Корзина ({{ cartTotalLength }})</span>
                    <span class="home-text mobile-view">Корзина</span>
                  </router-link>
                </div>
                <router-link to="/" class="home-register-mobile mr-2 mt-2 button mobile-hide">
                  <span class="home-text">+7 (982) 727-12-12</span>
                </router-link>
              </div>
            </div>
            <div class="home-container8 mt-6 mb-6">
              <button type="button" class="home-button button">
                <img src="http://127.0.0.1:8000/media/uploads/left.png" class="array-button">
              </button>
              <img
                alt="image"
                src="http://127.0.0.1:8000/media/uploads/adv.png"
                class="home-image"
              />
              <button type="button" class="home-button button">
                <img src="http://127.0.0.1:8000/media/uploads/right.png" class="array-button">
              </button>
            </div>
            </div>
        </div>
      </header>
      <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
        <div class="lds-dual-ring"></div>
      </div>
      <router-view/>
      <footer class="footer-custom">
        <div class="footer-title home-text-title">Теплый дом</div>
        <div class="footer-menu">
          <div class="home-text-black footer-menu-header">Покупателям
            <router-link to="/" class="footer-inmenu-bar">Частые вопросы</router-link>
            <router-link to="/" class="footer-inmenu-bar">Акции и скидки</router-link>
            <router-link to="/" class="footer-inmenu-bar">Установка и сервис</router-link>
          </div>
          <div class="home-text-black footer-menu-header">О компании
            <router-link to="/" class="footer-inmenu-bar">Политика компании</router-link>
            <router-link to="/" class="footer-inmenu-bar">Пресс-центр</router-link>
            <router-link to="/" class="footer-inmenu-bar">Документация</router-link>
          </div>
          <div class="home-text-black footer-menu-header">Контакты
            <router-link to="/" class="footer-inmenu-bar">Whatsapp</router-link>
            <router-link to="/" class="footer-inmenu-bar">Telegramm</router-link>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength +=  this.cart.items[i].quantity
      }
      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.button:hover{
  box-shadow: none;
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
.home-container {
  overflow-x: hidden;
  overflow-y: hidden;
  margin: auto;
  margin-top: 30px;
  width: 100%;
  max-width: 1024px;
  display: flex;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  align-content: space-between
}
.home-navbar-interactive {
  height: var(--dl-size-size-xxlarge);
  display: flex;
  align-items: center;
  padding: var(--dl-space-space-twounits) var(--dl-space-space-threeunits);
  justify-content: space-between;
}
.home-desktop-menu {
  flex: 1;
  display: flex;
  align-self: center;
  margin-left: var(--dl-space-space-unit);
  margin-right: var(--dl-space-space-unit);
}
.home-container1 {
  flex: 0 0 auto;
  display: flex;
  position: relative;
  align-self: center;
  align-items: center;
  margin-left: var(--dl-space-space-twounits);
  margin-right: var(--dl-space-space-twounits);
  padding-left: var(--dl-space-space-unit);
  padding-right: var(--dl-space-space-unit);
  flex-direction: column;
  justify-content: center;
}
.footer-menu{
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
  gap: 50px;
}
.footer-menu-header{
  display: flex;
  flex-direction: column;
}
.footer-inmenu-bar{
  margin: 2px;
  font-style: normal;
  font-weight: 100;
  font-size: 13px;
  text-transform: uppercase;
  color: #000000;
}
.footer-custom{
  margin-top: 10px;
  width: 100%;
  border-top: thick solid #ff6b00;
  display: flex;
  padding: 20px 20px 96px;
  align-items: flex-start;
  flex-direction: column;
}
.array-button{
  margin: 5px;
  height: 150px;
  width: 25px;
}
.home-container2 {
  flex: 0 0 auto;
  gap: 5%;
  display: flex;
  align-self: center;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  padding-left: var(--dl-space-space-threeunits);
  margin-bottom: var(--dl-space-space-unit);
  padding-right: var(--dl-space-space-threeunits);
  justify-content: space-around;
}
.home-container3 {
  flex: 0 0 auto;
  height: auto;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}
.home-container4 {
  flex: 0 0 auto;

  height: auto;
  display: flex;
  align-items: flex-start;
  margin-bottom: var(--dl-space-space-unit);
  justify-content: space-between;
}
.home-register {
  color: #ff6b00;
  width: var(--dl-size-size-large);
  border-color: #ff6b00;
  border-width: 3px;
  border-radius: 8px;
}
.home-register:hover, .home-register:focus {
  border-color: #595959;
}
.home-text {
  margin: 5px;
  font-style: normal;
  font-weight: 800;
  text-transform: uppercase;
  color: #ff6b00;
}
.home-register:hover .home-text, .home-register:focus .home-text{
  color: #595959;
}
.home-text-black {
  margin: 5px;
  font-style: normal;
  font-weight: 800;
  text-transform: uppercase;
  color: #000000;
}
.home-text-category {
  margin: 5px;
  font-style: normal;
  font-weight: 800;
  text-transform: uppercase;
  color: #ffffff;
}
.home-text-title {
  color: #ff6b00;
  font-size: 34px;
  font-style: normal;
  text-align: center;
  font-weight: 900;
  margin-bottom: var(--dl-space-space-unit);
  text-transform: uppercase;
}
.home-register2 {
  margin-right: 2px;
  color: #ffffff;
  width: var(--dl-size-size-xlarge);
  padding: 0.5rem;
  align-self: center;
  text-align: center;
  background-color: #ff6b00;
  border-radius: 8px;
}
.home-container5 {
  flex: 0 0 auto;
  width: auto;
  display: flex;
  align-items: center;
  margin-left: var(--dl-space-space-unit);
  margin-right: var(--dl-space-space-unit);
  padding-left: var(--dl-space-space-unit);
  padding-right: var(--dl-space-space-unit);
  flex-direction: column;
}
.home-textinput {
  color: transparent;
  width: var(--dl-size-size-xxlarge);
  margin-top: 0px;
  margin-left: var(--dl-space-space-unit);
  margin-right: var(--dl-space-space-unit);
  outline: none;
  border: none;
  box-shadow: none;
}
.home-search{
  display: flex;
  width: auto;
  height: auto;
  color: transparent;
  border-radius: 8px;
  border: 3px solid #ff6b00;
  border-radius: 8px;
}
.search-button{
  height: var(--dl-size-size-xlarge);
}
.home-register-mobile {
  color: #ff6b00;
  width: var(--dl-size-size-xlarge);
  padding: 0.5rem;
  align-self: center;
  text-align: center;
  border: #FFFFFF;
  background-color: #ffffff;
}
.home-container8 {
  flex: 0 0 auto;
  height: 100%;
  max-width: 1024px;
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  margin-left: var(--dl-space-space-unit);
  margin-right: var(--dl-space-space-unit);
  justify-content: center;
}
.home-button {
  width: var(--dl-size-size-small);
  height: var(--dl-size-size-large);
  border-width: 0px;
}
.home-image {
  width: 75%;
  height: var(--dl-size-size-large);
  object-fit: cover;
}
.home-icon {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
}
.home-nav {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.home-buttons {
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.home-login {
  margin-right: var(--dl-space-space-twounits);
}
.mobile-view{
  display: none;
}
@media screen and (max-width: 915px){
  .mobile-hide{
    display: none;
  }
  .mobile-view{
    display: flex;
  }
  .home-container3{
    align-items: flex-start;
  }
  .home-container3 .ml-2{
    margin-left: 0 !important;
  }
}
@media screen and (max-width: 660px) {
  .home-container5{
    justify-content: space-between
  }
  .home-register{
    width: 70px;
    height: 27px;
    border-radius: 5px;
  }
  .home-text{
    font-size: 10px;
  }
  .home-text-title{
    font-size: 20px;
  }
  .fa-shopping-cart{
    display: none;
  }
  .shopping-cart{
	display: none;
    padding-left: 0;
    padding-right: 0;
  }
  .home-register2{
    width: 80px;
    height: 30px;
    border-radius: 5px;
  }
  .home-register2 img{
    width: 10px;
    height: 14px;
  }
  .home-text-category{
    font-size: 11px;
  }
  .home-search{
    width: 147px;
    height: 30px;
    border-radius: 5px;
  }
  .home-textinput{
    height: auto;
    width: 120px;
  }
  .search-button{
    width: 20px;
    height: 20px;
  }
}

</style>
