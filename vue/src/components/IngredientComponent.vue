<template>
    <tr>
        <template v-if="ingredient.is_header">
            <td colspan="5" @click="done">
                <b>{{ ingredient.note }}</b>
            </td>
        </template>

        <template v-else>
            <td class="d-print-non" v-if="detailed" @click="done">
                <i class="far fa-check-circle text-success" v-if="ingredient.checked"></i>
                <i class="far fa-check-circle text-primary" v-if="!ingredient.checked"></i>
            </td>
            <td class="text-nowrap" @click="done">
                <span v-if="ingredient.amount !== 0" v-html="calculateAmount(ingredient.amount)"></span>
            </td>
            <td @click="done">
                <span v-if="ingredient.unit !== null && !ingredient.no_amount">{{ ingredient.unit.name }}</span>
            </td>
            <td @click="done">
                <template v-if="ingredient.food !== null">
                    <a :href="resolveDjangoUrl('view_recipe', ingredient.food.recipe.id)" v-if="ingredient.food.recipe !== null" target="_blank" rel="noopener noreferrer">{{ ingredient.food.name }}</a>
                    <span v-if="ingredient.food.recipe === null">{{ ingredient.food.name }}</span>
                </template>
            </td>
            <td v-if="detailed">
                <div v-if="ingredient.note">
                    <span v-b-popover.hover="ingredient.note" class="d-print-none touchable">
                        <i class="far fa-comment"></i>
                    </span>

                    <div class="d-none d-print-block"><i class="far fa-comment-alt d-print-none"></i> {{ ingredient.note }}</div>
                </div>
            </td>
        </template>
    </tr>
</template>

<script>
import { calculateAmount, ResolveUrlMixin, ApiMixin } from "@/utils/utils"

export default {
    name: "IngredientComponent",
    components: { },
    props: {
        ingredient: Object,
        ingredient_factor: { type: Number, default: 1 },
        detailed: { type: Boolean, default: true },
    },
    mixins: [ResolveUrlMixin, ApiMixin],
    data() {
        return {
            checked: false,
            dirty: undefined,
        }
    },
    watch: {
        ingredient: {
            handler() {},
            deep: true,
        }
    },
    mounted() {
    },
    computed: {
    },
    methods: {
        calculateAmount: function (x) {
            return calculateAmount(x, this.ingredient_factor)
        },
        // sends parent recipe ingredient to notify complete has been toggled
        done: function () {
            this.$emit("checked-state-changed", this.ingredient)
        },
    },
}
</script>

<style scoped>
/* increase size of hover/touchable space without changing spacing */
.touchable {
    padding-right: 2em;
    padding-left: 2em;
    margin-right: -2em;
    margin-left: -2em;
}
</style>
