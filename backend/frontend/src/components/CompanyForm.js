import api from '../api/axios';

// Use this instead of plain axios
const createCompany = async (companyData) => {
    try {
        const response = await api.post('/api/companies/', companyData);
        // Handle success
    } catch (error) {
        // Handle error
    }
}; 