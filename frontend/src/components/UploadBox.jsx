export default function UploadBox({
  onUpload
}) {

  return (
    <div>
      <input 
        type="file"
        onChange={(e) =>
          onUpload(e.target.files[0])
        }/>
    </div>
  )

}