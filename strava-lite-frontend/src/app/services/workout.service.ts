import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WorkoutService {
  private baseUrl = 'http://127.0.0.1:5000'; // Flask backend URL

  constructor(private http: HttpClient) {}

  getWorkouts(userId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/user/${userId}`);
  }
}