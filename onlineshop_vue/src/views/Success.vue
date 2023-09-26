<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Благодарим за заказ!</h1>

                <p>Ваш заказ принят в обработку, по завершению с вами свяжется наш оператор!</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Успешно | Магазин штук'
    },
}
</script>