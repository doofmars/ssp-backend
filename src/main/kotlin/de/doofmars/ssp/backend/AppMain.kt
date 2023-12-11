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
import com.codahale.metrics.Slf4jReporter
import io.ktor.server.metrics.dropwizard.*
import java.util.concurrent.TimeUnit
import io.ktor.server.routing.*
import de.doofmars.ssp.backend.apis.GameApi
import de.doofmars.ssp.backend.apis.LobbyApi
import io.ktor.server.engine.*
import io.ktor.server.metrics.dropwizard.*
import io.ktor.server.netty.*

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::main)
        .start(wait = true)
}

fun Application.main() {
    install(DefaultHeaders)
    // install open api spec plugin
    install(OpenAPIGen) {
        // configure open api spec here
        info {
            version = "1.0.0"
            title = "Swagger Petstore"
            description = "A sample API that uses a petstore as an example to demonstrate features in the swagger-koa library"
            contact {
                name = "Swagger API Team"
                email = "
//    install(DropwizardMetrics) {
//        val reporter = Slf4jReporter.forRegistry(registry)
//            .outputTo(this@main.log)
//            .convertRatesTo(TimeUnit.SECONDS)
//            .convertDurationsTo(TimeUnit.MILLISECONDS)
//            .build()
//        reporter.start(10, TimeUnit.SECONDS)
//    }
    install(ContentNegotiation) {
        register(ContentType.Application.Json, GsonConverter())
    }
    install(AutoHeadResponse) // see https://ktor.io/docs/autoheadresponse.html
    install(Compression, ApplicationCompressionConfiguration()) // see https://ktor.io/docs/compression.html
    install(HSTS, ApplicationHstsConfiguration()) // see https://ktor.io/docs/hsts.html
    install(Resources)
    install(Routing) {
        GameApi()
        LobbyApi()
    }

}
