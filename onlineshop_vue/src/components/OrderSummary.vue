<template>
  <div className="box mb-4">
    <h3 className="is-size-4 mb-6">Заказ #{{ order.id }}</h3>

    <h4 className="is-size-5">Товары</h4>

    <table className="table is-fullwidth">
      <thead>
      <tr>
        <th>Товар</th>
        <th>Цена</th>
        <th>Количество</th>
        <th>Итого</th>
      </tr>
      </thead>

      <tbody>
      <tr
          v-for="item in order.items"
          v-bind:key="item.product.id"
      >
        <td>{{ item.product.name }}</td>
        <td>{{ item.product.price }} руб.</td>
        <td>{{ item.quantity }}</td>
        <td>{{ getItemTotal(item).toFixed(2) }} руб.</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'OrderSummary',
  props: {
    order: Object
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    orderTotalLength(order) {
      return order.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
  }
}
</script>