import { Component, OnInit, inject } from '@angular/core';
import { UserService } from '../services/user.service';
import { WorkoutService } from '../services/workout.service';
import { CommonModule } from '@angular/common';

interface User {
  id: number;
  name: string;
  age: number;
}

interface Workout {
  date: string;
  time: string;
  distance: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  imports: [CommonModule]
})
export class HomeComponent implements OnInit {
  private userService: UserService = inject(UserService);
  private workoutService: WorkoutService = inject(WorkoutService);

  users: User[] = [];
  workouts: Workout[] = [];
  selectedUserId: number | null = null;

  ngOnInit(): void {
    this.fetchUsers();
  }

  fetchUsers(): void {
    this.userService.getUsers().subscribe({
      next: (users: User[]) => {
        this.users = users;
        console.log('Users received:', this.users);
      },
      error: (error: any) => console.error('Error fetching users:', error)
    });
  }

  fetchWorkouts(userId: number): void {
    this.selectedUserId = userId;
    this.workoutService.getWorkouts(userId).subscribe({
      next: (workouts: Workout[]) => {
        this.workouts = workouts;
        console.log(`Workouts received for user ${userId}:`, this.workouts);
      },
      error: (error: any) => console.error(`Error fetching workouts for user ${userId}:`, error)
    });
  }

  fetchWorkoutsFromEvent(event: Event): void {
    const userId = Number((event.target as HTMLSelectElement).value);
    if (userId) {
      this.fetchWorkouts(userId);
    }
  }
}            