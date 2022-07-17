<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-9">
                <h1 class="title">My account</h1>
            </div>
            <div class="column is-3">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>
            <div class="column is-8 is-offset-3">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Student Id</label>
                        <div class="control">
                            <input type="text" class="input" v-model="student_id">
                        </div>
                    </div>
                    <div class="field">
                        <label>how do you evaluate the professor's technological mastery?</label>
                        <div class="control">
                            <select class="select" v-model="q1">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>how do you evaluate the professor's teaching style?</label>
                        <div class="control">
                            <select class="select" v-model="q2">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>Does the professor come to class on time?</label>
                        <div class="control">
                            <select class="select" v-model="q3">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>How do you evaluate the interaction between the professor and the students?</label>
                        <div class="control">
                            <select class="select" v-model="q4">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>How do you evaluate the professor's grading method?</label>
                        <div class="control">
                            <select class="select" v-model="q5">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                    <div class="field">
                        <label>Does the professor take periodic exams?</label>
                        <div class="control">
                            <select class="select" v-model="q6">
                                <option value="good">Good</option>
                                <option value="average">Average</option>
                                <option value="bad">Bad</option>
                            </select>
                        </div>
                    </div>
                     <div class="field">
                        <label>Anything dosent mention in questions</label>
                        <div class="control">
                            <input type="text" class="input" v-model="q7">
                        </div>
                    </div>
                    <div class="field">
                        <div class="controll">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    data() {
        return {
            student_id: '',
            q1:'',
            q2:'',
            q3:'',
            q4:'',
            q5:'',
            q6:'',
            q7:'',
        }
    },
    methods: {
        async submitForm() {
            console.log("submit form")
            const result={
                student_id:this.student_id,
                q1:this.q1,
                q2:this.q2,
                q3:this.q3,
                q4:this.q4,
                q5:this.q5,
                q6:this.q6,
                q7:this.q7,
            }
            await axios
              .post('/api/v1/results/',result)
              .then(response=>{
                console.log(response)
              })
        },
        async logout() {
            await axios
                .post('/api/v1/token/logout')
                .then(response => {
                    console.log('logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>