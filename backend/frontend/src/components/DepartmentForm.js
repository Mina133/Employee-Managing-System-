const createDepartment = async () => {
    try {
        const departmentData = {
            name: "Department Name",
            company: companyId  // This should be a valid company ID
        };
        const response = await api.post('/api/departments/', departmentData);
        // Handle success
    } catch (error) {
        // Handle error
    }
}; 