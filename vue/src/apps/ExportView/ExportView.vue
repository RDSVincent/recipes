<template>
    <div id="app">
        <h2>{{ $t("Export") }}</h2>
        <div class="row">
            <div class="col col-md-12">
                <br />
                <!-- TODO get option dynamicaly -->
                <select class="form-control" v-model="recipe_app">
                    <option value="DEFAULT">Default</option>
                    <option value="SAFFRON">Saffron</option>
                    <option value="RECIPESAGE">Recipe Sage</option>
                    <option value="PDF">PDF (experimental)</option>
                </select>

                <br />
                <b-form-checkbox v-model="export_all" @change="disabled_multiselect = $event" name="check-button" switch style="margin-top: 1vh">
                    {{ $t("All recipes") }}
                </b-form-checkbox>

                <!-- <multiselect
                    :searchable="true"
                    :disabled="disabled_multiselect"
                    v-model="recipe_list"
                    :options="recipes"
                    :close-on-select="false"
                    :clear-on-select="true"
                    :hide-selected="true"
                    :preserve-search="true"
                    placeholder="Select Recipes"
                    :taggable="false"
                    label="name"
                    track-by="id"
                    id="id_recipes"
                    :multiple="true"
                    :loading="recipes_loading"
                    @search-change="searchRecipes"
                >
                </multiselect> -->
                <generic-multiselect
                    class="input-group-text m-0 p-0"
                    @change="recipe_list = $event.val"
                    label="name"
                    :model="Models.RECIPE"
                    style="flex-grow: 1; flex-shrink: 1; flex-basis: 0"
                    v-bind:placeholder="$t('Recipe')"
                    :limit="20"
                    :multiple="true"
                />
                <generic-multiselect
                    @change="filter = $event.val"
                    :model="Models.CUSTOM_FILTER"
                    style="flex-grow: 1; flex-shrink: 1; flex-basis: 0"
                    :placeholder="$t('Custom Filter')"
                    :multiple="false"
                    :limit="50"
                />

                <br />
                <button @click="exportRecipe()" class="btn btn-primary shadow-none"><i class="fas fa-file-export"></i> {{ $t("Export") }}</button>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from "vue"
import { BootstrapVue } from "bootstrap-vue"

import "bootstrap-vue/dist/bootstrap-vue.css"

import LoadingSpinner from "@/components/LoadingSpinner"

import { StandardToasts, makeToast, resolveDjangoUrl, ApiMixin } from "@/utils/utils"
// import Multiselect from "vue-multiselect"
import GenericMultiselect from "@/components/GenericMultiselect"
import { ApiApiFactory } from "@/utils/openapi/api.ts"
import axios from "axios"

Vue.use(BootstrapVue)

export default {
    name: "ExportView",
    /*mixins: [
    ResolveUrlMixin,
    ToastMixin,
  ],*/
    components: { GenericMultiselect },
    mixins: [ApiMixin],
    data() {
        return {
            export_id: window.EXPORT_ID,
            loading: false,
            disabled_multiselect: false,

            recipe_app: "DEFAULT",
            recipe_list: [],
            recipes_loading: false,
            recipes: [],
            export_all: false,
            filter: undefined,
        }
    },
    mounted() {
        if (this.export_id) this.insertRequested()
        // else this.searchRecipes("")
    },
    methods: {
        insertRequested: function () {
            let apiFactory = new ApiApiFactory()

            this.recipes_loading = true

            apiFactory
                .retrieveRecipe(this.export_id)
                .then((response) => {
                    this.recipes_loading = false
                    this.recipe_list.push(response.data)
                })
                .catch((err) => {
                    console.log(err)
                    StandardToasts.makeStandardToast(StandardToasts.FAIL_FETCH)
                })
            // .then((e) => this.searchRecipes(""))
        },

        // searchRecipes: function (query) {
        //     this.recipes_loading = true

        //     this.genericAPI(this.Models.RECIPE, this.Actions.LIST, { query: query })
        //         .then((response) => {
        //             this.recipes = response.data.results
        //             this.recipes_loading = false
        //         })
        //         .catch((err) => {
        //             console.log(err)
        //             StandardToasts.makeStandardToast(StandardToasts.FAIL_FETCH)
        //         })
        // },

        exportRecipe: function () {
            if (this.recipe_list.length < 1 && this.export_all == false && this.filter === undefined) {
                makeToast(this.$t("Error"), this.$t("Select at least one recipe"), "danger")
                return
            }

            this.error = undefined
            this.loading = true
            let formData = new FormData()
            formData.append("type", this.recipe_app)
            formData.append("all", this.export_all)
            formData.append("filter", this.filter?.id ?? null)

            for (var i = 0; i < this.recipe_list.length; i++) {
                formData.append("recipes", this.recipe_list[i].id)
            }

            axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded"
            axios
                .post(resolveDjangoUrl("view_export"), formData)
                .then((response) => {
                    if (response.data["error"] !== undefined) {
                        makeToast(this.$t("Error"), response.data["error"], "warning")
                    } else {
                        window.location.href = resolveDjangoUrl("view_export_response", response.data["export_id"])
                    }
                })
                .catch((err) => {
                    this.error = err.data
                    this.loading = false
                    console.log(err)
                    makeToast(this.$t("Error"), this.$t("There was an error loading a resource!"), "warning")
                })
        },
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style></style>
