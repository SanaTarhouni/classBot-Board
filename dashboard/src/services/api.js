import axios from 'axios'
export default () => {
  return axios.create({
    baseURL: `https://etvkxv62j9.execute-api.us-east-1.amazonaws.com/api`
  })
}