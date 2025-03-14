import { FormGroup } from "@angular/forms";

export const checkInputForm = (formGroup:FormGroup, formKey:string, errorCode:string)=>{
    return (formGroup.get(formKey)?.dirty || formGroup.get(formKey)?.touched) && formGroup.get(formKey)?.hasError(errorCode)
}