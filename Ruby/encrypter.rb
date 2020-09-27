class Rot
    attr_reader :nombre
    def initialize
        @nombre = "Rot"
    end
    def encriptar palabra, n
        n_palabra = ""
        palabra.each_byte do |ascii|
            if ascii != 32
                if ascii + n > 122
                    ascii -= 26
                end
                ascii += n
            end
            n_palabra += ascii.chr
        end
        return n_palabra
    end
    def desencriptar palabra, n
        n_palabra = ""
        palabra.each_byte do |ascii|
            if ascii != 32
                if ascii - n < 97
                    ascii += 26
                end
                ascii -= n
            end
            n_palabra += ascii.chr
        end
        return n_palabra
    end
end

class SimpleTranspose
    attr_reader :nombre
    def initialize
        @nombre = "SimpleTranspose"
    end
    def encriptar palabra, n
        n_palabra = ""
        i = palabra.length - n
        terminado = false
        while not terminado
            n_palabra += palabra[i]
            i += 1
            if i == palabra.length
                i = 0
            end
            if i == palabra.length - n
               terminado = true
            end
        end
        return n_palabra
    end
    def desencriptar palabra, n
        n_palabra = ""
        i = n - 1
        terminado = false
        while not terminado
            n_palabra = palabra[i] + n_palabra
            i -= 1
            if i == -1
                i = palabra.length - 1
            end
            if i == n - 1
               terminado = true
            end
        end
        return n_palabra
    end
end

class Decorator
    def initialize decorador
        @decorador = decorador
    end
    def encriptar palabra, n
        puts "Ejecutando " + @decorador.nombre + " en sentido encriptación.\n"
        return @decorador.encriptar palabra, n
    end
    def desencriptar palabra, n
        puts "Ejecutando " + @decorador.nombre + " en sentido desencriptación.\n"
        return @decorador.desencriptar palabra, n
    end
end 

class Cipher
    def initialize lista
        @lista = lista
        @Rot = Decorator.new(Rot.new)
        @SimpleTranspose = Decorator.new(SimpleTranspose.new)
    end
    def encrypt palabra
        n_palabra = palabra
        @lista.each do |tupla|
            if tupla[0] == "R"
                n_palabra = @Rot.encriptar n_palabra, tupla[1]
            else
                n_palabra = @SimpleTranspose.encriptar n_palabra, tupla[1]
            end
        end
        return n_palabra
    end
    def decrypt palabra
        n_palabra = palabra
        lista = @lista.reverse
        lista.each do |tupla|
            if tupla[0] == "R"
                n_palabra = @Rot.desencriptar n_palabra, tupla[1]
            else
                n_palabra = @SimpleTranspose.desencriptar n_palabra, tupla[1]
            end
        end
        return n_palabra
    end
end

def get_random_cipher
    lista = []
    i = 0
    while 0 <= i && i <= 80
        n = rand(1..10)
        metodo = ['R', 'S'].sample
        lista << [metodo, n]
        i = rand(1..100)
    end
    Cipher.new(lista)
end

cypher = get_random_cipher
puts "hola mundo"
encriptada = cypher.encrypt "hola mundo"
puts encriptada
puts cypher.decrypt encriptada
#puts Rot "hola mundo", 13
#puts dRot "ubyn zhaqb", 13
#puts SimpleTranspose "hola mundo", 3
#puts dSimpleTranspose "ndohola mu", 3
