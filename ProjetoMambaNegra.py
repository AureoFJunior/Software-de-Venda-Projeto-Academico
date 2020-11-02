from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import base64

#Encode class and array
class ObjUsuario():
    def __init__(self, senha):
        self.senha = senha    

    def ObterSenhaCriptografada(self):
        self.encoded_key= base64.b64encode(self.senha.encode())
        return self.encoded_key

usuariosEncodeList = list()
#Menu principal
menuInicial = Tk()

menuInicial.title('Mamba Negra')
menuInicial.geometry('600x370+700+200')
menuInicial.resizable(False, False)
menuInicial['bg'] = '#80ffaa'

listaUsuarioLog = []
#Menu de cadastro
def menuCadastroCriar():
    menuCadastro = Toplevel()
    menuCadastro.title('Mamba Negra - Cadastro')
    menuCadastro.geometry('450x350+700+200')
    menuCadastro.resizable(False, False)
    menuCadastro['bg'] = '#80ffaa'                  
    
    #Background do menu
    image2 = Image.open("..\dist\c0d9e140299087dfa9dbb652697dfe93.PNG")
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(menuCadastro, image=image1)
    background_label.image1=image1
    background_label['bg'] = '#80ffaa'
    background_label.place(x=10, y=0, height=580, width=650)

    labelCad = Label(menuCadastro, text ='Usuário: ',
        font='Impact 17',
        fg='#000000',
        bg='#80ffaa'
    )
    
    labelCad.grid(row=0,sticky=W)
    
    labelSenha = Label(menuCadastro, text ='Senha: ',
        font='Impact 17',
        fg='#000000',
        bg='#80ffaa'
    )
    
    labelSenha.grid(row=1,sticky=W)
    
    labelSenhaConfirma = Label(menuCadastro, text ='Confirma Senha: ',
        font='Impact 17',
        fg='#000000',
        bg='#80ffaa'
    )
    labelSenhaConfirma.grid(row=2,sticky=W)

    #entradas cadastro e login

    cadEntry = Entry(menuCadastro, width=30)
    cadEntry.grid(row=0, column=2, sticky=W)
    senhaEntry = Entry(menuCadastro, width=30)
    senhaEntry.grid(row=1, column=2, sticky=W)
    confirmaSenhaEntry = Entry(menuCadastro, width=30)
    confirmaSenhaEntry.grid(row=2, column=2, sticky=W)
    cadEntry.focus()

    btnConfirma = Button(menuCadastro, text='Confirmar Cadastro', width=20, font='Impact 15', command=lambda: confirmaCadastro())
    btnConfirma.grid(row=3, column=2, sticky=S)
    
    tipoUsuario = IntVar()
    radioTipoClie = Radiobutton(menuCadastro, text = 'Cliente', variable=tipoUsuario, value=1, bg='#80ffaa', font='Impact 17')
    radioTipoVen = Radiobutton(menuCadastro, text = 'Vendedor', variable=tipoUsuario, value=2, bg='#80ffaa',font='Impact 17')
    radioTipoInter = Radiobutton(menuCadastro, text = 'Intermediário', variable=tipoUsuario, value=3, bg='#80ffaa',font='Impact 17')
    radioTipoClie.select()
    radioTipoClie.grid(row=4, column=0, sticky=W)
    radioTipoVen.grid(row=5, column=0, sticky=W)
    radioTipoInter.grid(row=6, column=0, sticky=W)
    #Botão confirma cadastro   


    def validaEntrada():
        senhaUsuario = senhaEntry.get()
        senhaUsuarioConf = confirmaSenhaEntry.get() 
        usernameUsuario = cadEntry.get()
        
        if senhaUsuario != senhaUsuarioConf:
            return "Senha não confere!"

        elif len(str(usernameUsuario).strip()) <= 0:
            return "Usuário inválido!"

        elif len(str(usernameUsuario).strip()) >= 25:
            return "Limite de caracteres excedido!" 

        elif len(str(senhaUsuario).strip()) >= 25:
            return "Limite de caracteres excedido!" 

        elif len(str(senhaUsuario).strip()) <= 0:
            return "Senha inválida!"

        return ""

    
    def confirmaCadastro():
        senhaUsuario = senhaEntry.get()
        senhaUsuarioConf = confirmaSenhaEntry.get() 
        usernameUsuario = cadEntry.get()
        retorno = validaEntrada()
 

        for item in listaUsuarioLog:
            x = item.split(':', 1)
            if x[0] == usernameUsuario:
                messagebox.showerror('ERROR','Usuário já está em uso!')
   
        if len(retorno) == 0:
            messagebox.showinfo('Notification', 'Cadastro Efetuado!')
            listaUsuarioLog.append(usernameUsuario + ':' +  senhaUsuario)
            pessoa = ObjUsuario(senhaUsuario)
            pessoa.ObterSenhaCriptografada()
            usuariosEncodeList.append(pessoa) 
            for gente in usuariosEncodeList:
                codados = gente.ObterSenhaCriptografada()
            menuCadastro.destroy()
      
        else:
            messagebox.showerror('!ERROR!', 'Cadastro não efetivado, Motivo: ' + f'{retorno}')   

#Menu Login
def menuLoginCriar():
    menuLogin = Toplevel()
    menuLogin.title('Mamba Negra - Login')
    menuLogin.geometry('450x350+700+200')
    menuLogin.resizable(False, False)
    menuLogin['bg'] = '#80ffaa'                  
    
    #Background do menu
    image2 = Image.open("..\dist\Sign_In-512.png")
    image1 = ImageTk.PhotoImage(image2)
    background_label = Label(menuLogin, image=image1)
    background_label.image1=image1
    background_label['bg'] = '#80ffaa'
    background_label.place(x=10, y=0, height=580, width=650)

    labelUsername = Label(menuLogin, text ='Usuário: ',
        font='Impact 17',
        fg='#000000',
        bg='#80ffaa'
    )
    
    labelUsername.grid(row=0,sticky=W)
    
    labelPassword = Label(menuLogin, text ='Senha: ',
        font='Impact 17',
        fg='#000000',
        bg='#80ffaa'
    )
    
    labelPassword.grid(row=1,sticky=W)
    
    btnConfirmaLog = Button(menuLogin, text='Entrar', width=20, font='Impact 15', command=lambda: confirmaLogin())
    btnConfirmaLog.grid(row=3, column=2, sticky=S)

    usernameEntry = Entry(menuLogin, width=30)
    usernameEntry.grid(row=0, column=2, sticky=W)
    passwordEntry = Entry(menuLogin, width=30)
    passwordEntry.grid(row=1, column=2, sticky=W)

    def confirmaLogin():
        usernamelog = usernameEntry.get()
        passwordLog = passwordEntry.get()

        item = usernamelog + ":" + passwordLog
        if item in listaUsuarioLog:
            messagebox.showinfo('Notification', 'Logado!')
            menuLogin.destroy()
            
        else:
            messagebox.showerror('!ERROR!', 'Usuário ou senha inválidos!')  
# Menu primário

botCad = Button(menuInicial, text = 'Cadastro',
    font='Impact 30 italic',
    bg='#99ffbb',
    fg='#262626',
    width=30,
    justify=CENTER,
    command =lambda: menuCadastroCriar()
    )
botLog = Button(menuInicial, text = 'Login',
    font='Impact 30 italic',
    bg='#99ffbb',
    fg='#262626',
    width=30,
    justify=CENTER,
    command=lambda: menuLoginCriar()
    )
botExit = Button(menuInicial, text = 'Sair',
    font='Impact 30 italic',
    bg='#99ffbb',
    fg='#262626',
    width=30,
    justify=CENTER,
    command =lambda: quit()
    )
labelTitle = Label(menuInicial, text = 'Escolha uma opção\n',
    font='Impact 30 italic',
    bg='#66ff99',
    fg='#000000',
    width=30,
    bd=10,
    relief='raised'
    )

labelTitle.pack()
botCad.pack()
botLog.pack()
botExit.pack()

menuInicial.mainloop()