from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="TUGAS 1 INTEGRASI SISTEM",
    description="API Data Mahasiswa dengan fitur CRUD lengkap",
    version="1.0.0"
)

# 1. Model Data (Sesuai instruksi tugas)
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# 2. Database Sementara
db_mahasiswa: Dict[int, Mahasiswa] = {}

@app.get("/")
def root():
    return {"message": "API Tugas 1 Integrasi Sistem Berjalan"}

# 3. CREATE (POST)
@app.post("/mahasiswa/{id}", response_model=Mahasiswa, status_code=201)
def create_mahasiswa(id: int, data: Mahasiswa):
    if id in db_mahasiswa:
        raise HTTPException(status_code=400, detail=f"Mahasiswa dengan ID {id} sudah ada!")
    db_mahasiswa[id] = data
    return data

# 4. READ ALL (GET)
@app.get("/mahasiswa/")
def get_all_mahasiswa():
    return {"total": len(db_mahasiswa), "data": db_mahasiswa}

# 5. READ BY ID (GET)
@app.get("/mahasiswa/{id}", response_model=Mahasiswa)
def get_mahasiswa_by_id(id: int):
    if id not in db_mahasiswa:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    return db_mahasiswa[id]

# 6. UPDATE (PUT)
@app.put("/mahasiswa/{id}", response_model=Mahasiswa)
def update_mahasiswa(id: int, data: Mahasiswa):
    if id not in db_mahasiswa:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    db_mahasiswa[id] = data
    return data

# 7. DELETE (DELETE)
@app.delete("/mahasiswa/{id}")
def delete_mahasiswa(id: int):
    if id not in db_mahasiswa:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    del db_mahasiswa[id]
    return {"message": f"Data mahasiswa dengan ID {id} berhasil dihapus"}