from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel
from model import Comprador

app = FastAPI()

class CompradorModel(BaseModel):
    idComprador: int
    cpf: str
    name: str
    email: str

class FornecedorModel(BaseModel):
    idFornecedor: int
    name: str
    cnpj: str

class ProdutoModel(BaseModel):
    idProduto: int
    name: str
    idCategoria: int
    preco: str
    peso: int
    altura: int
    largura: int

class CategoriaModel(BaseModel):
    idCategoria: int
    name: str
    categoria_tipo: str

#Persistence
compradores = []
fornecedores = []
categorias = []
produtos = []

#API - Comprador ----------------------------------------------------------------------------------
@app.post('/comprador', status_code=status.HTTP_201_CREATED)
def AdicionarComprador(comprador: CompradorModel):
    compradores.append(comprador)

@app.get('/comprador')
def ListarComprador():
    return compradores

@app.delete('/comprador/{idComprador}', status_code=status.HTTP_204_NO_CONTENT)
def ApagarComprador(idComprador: int):
    resultado = list(filter(lambda x: x.idComprador == idComprador, enumerate(compradores)))
    if resultado:
        compradores.remove(resultado.index[0])
        #return resultado
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Comprador não encontrado')

@app.put('/comprador/{cpf}')
def AlterarComprador(cpf: str, comprador: CompradorModel):
    busca_comprador = list(filter(lambda x: x.cpf == cpf, compradores))

    if not busca_comprador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Comprador com cpf: {cpf} nao encontrado')

    comprador_alterado = busca_comprador[0]
    comprador_alterado.name = comprador.name
    comprador_alterado.email = comprador.cpf
    comprador_alterado.cpf = comprador.cpf

    return comprador_alterado
        
@app.patch('/comprador/alterar-cpf/{cpf}')
def AlterarCPF(cpf: str, cpf_novo: str = Body(...)):
    resultado = list(filter(lambda x: x.cpf == cpf, compradores))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details='CPF não encontrado')

    comprador_encontrado = resultado[0] 
    comprador_encontrado.cpf = cpf_novo

    return comprador_encontrado   


#API - Fornecedor ----------------------------------------------------------------------------------
@app.get('/fornecedor')
def ListarFornecedor():
    return fornecedores

@app.post('/fornecedor', status_code=status.HTTP_201_CREATED)
def AdicionarFornecedor(fornecedor: FornecedorModel):
    fornecedores.append(fornecedor)

@app.delete('/fornecedor/{cnpj}', status_code=status.HTTP_204_NO_CONTENT)
def ApagarFornecedor(cnpj: str):
    fornecedor_encontrado = list(filter(lambda x: x.cnpj == cnpj, enumerate(fornecedores)))
    if fornecedor_encontrado:
        fornecedores.remove(fornecedor_encontrado.index[0])
        #return fornecedor_encontrado
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Fornecedor não encontrado')


#API - Categoria ----------------------------------------------------------------------------------
@app.get('/categoria')
def ListarCategoria():
    return categorias

@app.post('/categoria', status_code=status.HTTP_201_CREATED)
def AdicionarCategoria(categoria: CategoriaModel):
    categorias.append(categoria)

@app.delete('/categoria/{idCategoria}', status_code=status.HTTP_204_NO_CONTENT)
def ApagarFornecedor(idCategoria: str):
    categoria_encontrada = list(filter(lambda x: x.idCategoria == idCategoria, enumerate(categorias)))
    if categoria_encontrada:
        fornecedores.remove(categoria_encontrada.index[0])
        #return fornecedor_encontrado
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Categoria não encontrada')
 
# #API - Produto ----------------------------------------------------------------------------------    
@app.get('/produto')
def ListarProduto():
    return produtos

@app.post('/produto', status_code=status.HTTP_201_CREATED)
def AdicionarProduto(produto: ProdutoModel):
    produtos.append(produto)

@app.delete('/produto/{cnpj}', status_code=status.HTTP_204_NO_CONTENT)
def ApagarProduto(idProduto: int):
    produto_encontrado = list(filter(lambda x: x.idProduto == idProduto, enumerate(produtos)))
    if produto_encontrado:
        produtos.remove(produto_encontrado.index[0])
        #return fornecedor_encontrado
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Fornecedor não encontrado')
