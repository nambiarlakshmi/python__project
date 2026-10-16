def scheduleJobs(T, L):
    jobs = list(range(len(T)))

    jobs.sort(key=lambda i: (L[i] / T[i], -i), reverse=True)

    return [i + 1 for i in jobs]
print(scheduleJobs([3, 1, 2], [1, 3, 2]))
#Chat GPT helped me