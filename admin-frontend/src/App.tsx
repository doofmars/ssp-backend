import React, {useState, useEffect} from 'react';
import './App.css';
import {Configuration, Game, CreateGame, LobbyApi} from "./api-client";

function App() {
    // Development configuration
    let openapiConfig = new Configuration(
        {
            basePath: process.env.REACT_APP_API_URL + "/api"
        }
    );
    let baseurl = process.env.REACT_APP_API_URL;
    // Production configuration, here we have a reverse proxy that redirects /api to the api server
    if (process.env.NODE_ENV === 'production') {
        baseurl = window.location.origin
        openapiConfig = new Configuration(
            {
                basePath: "/api"
            }
        );
    }
    const lobbyApi = new LobbyApi(openapiConfig);

    const [games, setGames] = useState<Game[]>([]);

    useEffect(() => {
        lobbyApi.gamesGet().then((res) => {
            setGames(res.data);
        }).catch((err) => {
            console.log(err);
        });
    }, []);

    const handleDelete = async (gameId: string) => {
        try {
            await lobbyApi.gameGameIdDelete(gameId);
            setGames(games.filter(game => game.id !== gameId));
        } catch (err) {
            console.log(err);
        }
    };

    const handleCreate = async () => {
        try {
            const createGame: CreateGame = {'host': {'name': 'test'}}
            await lobbyApi.gamePut(createGame).then((res) => {
                setGames([...games, res.data]);
            }).catch((err) => {
                console.log(err);
            });
        } catch (err) {
            console.log(err);
        }
    }

    return (
        <div className="App">
            <header className="App-header">
                <h1>Links</h1>
                <a href={baseurl + '/api/ui'}>Swagger UI {baseurl + '/api/ui'}</a>
                <div>
                    <a href={baseurl + '/express'}>Mongo Express {baseurl + '/express'}</a>
                    Username: <b>admin</b> Password: <b>example</b>
                </div>
                <h1>Games</h1>
                <div>
                    Create new game <button onClick={handleCreate}>Create</button>
                </div>
                <table>
                    <thead>
                    <tr>
                        <th>Id</th>
                        <th>Host Name</th>
                        <th>Guest Name</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {games.map((game) => (
                        <tr key={game.id}>
                            <td>{game.id}</td>
                            <td>{game.host?.name}</td>
                            <td>{game.guest?.name}</td>
                            <td>{game.status}</td>
                            <td>
                                <button>Edit</button>
                                <button onClick={() => handleDelete(game.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </header>
        </div>
    );
}

export default App;
