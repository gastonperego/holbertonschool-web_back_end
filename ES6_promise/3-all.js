import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then((result) => { process.stdout.write(`${result.body} `); });
  createUser()
    .then((result) => { console.log(`${result.firstName} ${result.lastName}`); });
}
