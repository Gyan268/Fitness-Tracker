import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app/app.component'; // ✅ Ensure correct path
import { provideRouter } from '@angular/router';
import { routes } from './app/app-routing.module'; // ✅ Ensure correct path


bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient() // ✅ This provides HttpClient globally
  ]
}).catch(err => console.error(err));