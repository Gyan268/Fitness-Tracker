import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Workout {
  date: string;
  time: string;
  distance: string;
}

export interface User {
  id: number;
  name: string;
  age: number;
  workouts: Workout[]; // ✅ Ensure 'workouts' exists
}

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  getUsers(): Observable<{ users: User[] }> {
    return this.http.get<{ users: User[] }>(`${this.apiUrl}/users`);
  }

  getUserById(userId: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/user/${userId}`);
  }
}