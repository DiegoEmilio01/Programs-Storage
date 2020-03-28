def true?(str)
    if str == "true" then true else false end
end

class Persona
    attr_reader :id, :nombre, :edad

    def initialize(id, nombre, edad)
        @id = id.to_i
        @nombre = nombre
        @edad = edad.to_i
    end
end

class Habitante < Persona
    attr_reader :sector

    def initialize(id, nombre, edad, sector)
        super(id, nombre, edad)
        @sector = sector
    end

    def cuarentena
        infectado = false
        if @edad >= 65
            infectado = true
        end
        if @sector.hay_infectados
            infectado = true
        end
        if infectado
            return true
        else
            return infectado
        end
    end
end

class Pasajero < Persona
    attr_reader :vuelos, :paises

    def initialize(id, nombre, edad, vuelos, paises)
        super(id, nombre, edad)
        @vuelos = vuelos
        @paises = paises
    end

    def cuarentena(chequear)
        infectado = false
        if (@edad >= 65) and (chequear == "todo")
            infectado = true
        end
        if  (chequear == "todo") or (chequear == "paises")
            lista_paises = []
            @paises.each do |pais|
                if pais.hay_infectados
                    infectado = true
                    lista_paises << pais.nombre
                elsif (chequear == "todo")
                    lista_paises << pais.nombre
                end
            end
        end
        if (chequear == "todo") or (chequear == "vuelos")
            lista_vuelos = []
            @vuelos.each do |vuelo|
                if vuelo.hay_infectados
                    infectado = true
                    lista_vuelos << vuelo.id.to_s
                elsif (vuelo.dias_desde_vuelo <= 14) and (chequear == "todo")
                    infectado = true
                    lista_vuelos << vuelo.id.to_s
                elsif chequear == "todo"
                    lista_vuelos << vuelo.id.to_s
                end
            end
        end
        if infectado and (chequear == "todo")
            return lista_paises.join(" - ") + ". " + @vuelos.length.to_s
        elsif infectado and (chequear == "paises")
            return lista_paises.join(" - ")
        elsif infectado and (chequear == "vuelos")
            return lista_vuelos.join(" - ")
        else
            return infectado
        end
    end
end

class Sector
    attr_reader :id, :hay_infectados

    def initialize(id, hay_infectados)
        @id = id.to_i
        @hay_infectados = true? hay_infectados
    end
end

class Vuelo
    attr_reader :id, :hay_infectados, :dias_desde_vuelo

    def initialize(id, hay_infectados, dias_desde_vuelo)
        @id = id.to_i
        @hay_infectados = true? hay_infectados
        @dias_desde_vuelo = dias_desde_vuelo.to_i
    end
end

class Pais
    attr_reader :id, :nombre, :hay_infectados

    def initialize(id, nombre, hay_infectados)
        @id = id.to_i
        @nombre = nombre
        @hay_infectados = true? hay_infectados
    end
end
