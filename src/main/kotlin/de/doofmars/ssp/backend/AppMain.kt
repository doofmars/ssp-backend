package de.doofmars.ssp.backend

import io.ktor.server.application.*
import io.ktor.serialization.gson.*
import io.ktor.http.*
import io.ktor.server.resources.*
import io.ktor.server.plugins.autohead.*
import io.ktor.server.plugins.compression.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.server.plugins.defaultheaders.*
import io.ktor.server.plugins.hsts.*
import io.ktor.server.routing.*
import de.doofmars.ssp.backend.apis.gameApi
import de.doofmars.ssp.backend.apis.lobbyApi
import io.github.smiley4.ktorswaggerui.SwaggerUI
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::main)
        .start(wait = true)
}

fun Application.main() {
    install(DefaultHeaders)
    // install open api spec plugin
    install(SwaggerUI) {
        swagger {
            swaggerUrl = "swagger-ui"
            forwardRoot = true
        }
        info {
            title = "SSP-Online Backend"
            version = "1.0.0"
            description = "This is a the backend for the SSP Online Game. It is a RESTful API that is used by the frontend to play the game."
        }
        server {
            url = "http://localhost:8080"
            description = "Development Server"
        }
    }
    install(ContentNegotiation) {
        register(ContentType.Application.Json, GsonConverter())
    }
    install(AutoHeadResponse) // see https://ktor.io/docs/autoheadresponse.html
    install(Compression, ApplicationCompressionConfiguration()) // see https://ktor.io/docs/compression.html
    install(HSTS, ApplicationHstsConfiguration()) // see https://ktor.io/docs/hsts.html
    install(Resources)
    install(Routing) {
        gameApi()
        lobbyApi()
    }

}
