export async function uploadPdf(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    "http://localhost:8000/upload",
    {
      method: "POST",
      body: formData,
    }
  );

  return await response.json();
}