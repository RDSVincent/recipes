<template>
    <span>
        <linked-recipe v-if="linkedRecipe" :item="item" />
        <icon-badge v-if="Icon" :item="item" />
        <on-hand-badge v-if="OnHand" :item="item" />
    </span>
</template>

<script>
import LinkedRecipe from "@/components/Badges/LinkedRecipe"
import IconBadge from "@/components/Badges/Icon"
import OnHandBadge from "@/components/Badges/OnHand"

export default {
    name: "CardBadges",
    components: { LinkedRecipe, IconBadge, OnHandBadge },
    props: {
        item: { type: Object },
        model: { type: Object },
    },
    data() {
        return {}
    },
    mounted() {},
    computed: {
        linkedRecipe: function () {
            return this.model?.badges?.linked_recipe ?? false
        },
        Icon: function () {
            return this.model?.badges?.icon ?? false
        },
        OnHand: function () {
            return this.model?.badges?.food_onhand ?? false
        },
    },
    watch: {},
    methods: {},
}
</script>
